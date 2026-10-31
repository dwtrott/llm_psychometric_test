"""Create a fully self-contained psychometric KG viewer. Python 3.10+, stdlib.
No model calls, scoring imports, network, or visualization packages required.
"""
import argparse, json, pathlib

def validate_graph(graph):
    if not isinstance(graph,dict) or graph.get('schema_version')!='0.1.0':
        raise ValueError('Expected processor graph schema_version 0.1.0')
    nodes=graph.get('nodes'); edges=graph.get('edges')
    if not isinstance(nodes,list) or not isinstance(edges,list): raise ValueError('nodes and edges must be arrays')
    if len(nodes)>100000 or len(edges)>300000: raise ValueError('Viewer limit: 100,000 nodes and 300,000 edges per profile')
    ids=set()
    for node in nodes:
        if not isinstance(node,dict) or not isinstance(node.get('id'),str) or not isinstance(node.get('kind'),str): raise ValueError('Every node needs string id and kind')
        if node['id'] in ids: raise ValueError('Duplicate node id: '+node['id'])
        ids.add(node['id'])
    for edge in edges:
        if not isinstance(edge,dict) or edge.get('source') not in ids or edge.get('target') not in ids or not isinstance(edge.get('type'),str): raise ValueError('Malformed edge or dangling endpoint')
    configs=[n for n in nodes if n['kind']=='model_configuration']
    runs=[n for n in nodes if n['kind']=='run']
    if len(configs)!=1 or len(runs)!=1: raise ValueError('Load one processor run/configuration per graph file')
    if graph.get('model_configuration')!=configs[0]['id']: raise ValueError('Configuration identity mismatch')
    if not graph.get('battery_hash'): raise ValueError('battery_hash is required for comparison')
    return graph

def build_viewer(graph_paths=(), output='psychometric-viewer.html', template=None):
    """Embed zero or more raw graph.json files; returned HTML also accepts local imports."""
    graphs=[]
    for path in graph_paths:
        p=pathlib.Path(path)
        if p.stat().st_size>80*1024*1024: raise ValueError('Graph file exceeds 80 MiB')
        graph=validate_graph(json.loads(p.read_text(encoding='utf-8-sig')))
        graphs.append({'filename':p.name,'graph':graph})
    source=pathlib.Path(template) if template else pathlib.Path(__file__).with_name('viewer.html')
    document=source.read_text(encoding='utf-8')
    marker='<!--PROFILE_PAYLOAD-->'
    if marker not in document: raise ValueError('Use the supplied unpopulated viewer.html template')
    # Escape script-closing sequences and HTML-sensitive characters from raw model text.
    payload=json.dumps(graphs,ensure_ascii=False,allow_nan=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    document=document.replace(marker,'<script type="application/json" id="embedded-profiles">'+payload+'</script>')
    destination=pathlib.Path(output)
    if destination.resolve()==source.resolve(): raise ValueError('Choose an output path other than the template')
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(document,encoding='utf-8')
    return destination

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('graphs',nargs='*',help='One processor graph.json per model/run')
    parser.add_argument('--out',default='psychometric-viewer.html')
    args=parser.parse_args()
    path=build_viewer(args.graphs,args.out)
    print('Saved '+str(path.resolve()))

if __name__=='__main__': main()
