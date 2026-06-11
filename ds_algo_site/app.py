from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trees')
def trees():
    return render_template('trees.html')

@app.route('/tree-algorithms')
def tree_algorithms():
    return render_template('tree_algorithms.html')

@app.route('/hashing')
def hashing():
    return render_template('hashing.html')

@app.route('/hash-algorithms')
def hash_algorithms():
    return render_template('hash_algorithms.html')

@app.route('/linked-lists')
def linked_lists():
    return render_template('linked_lists.html')

@app.route('/linked-list-algorithms')
def linked_list_algorithms():
    return render_template('linked_list_algorithms.html')

@app.route('/sorting')
def sorting():
    return render_template('sorting.html')

@app.route('/sorting-algorithms')
def sorting_algorithms():
    return render_template('sorting_algorithms.html')

@app.route('/queues-stacks')
def queues_stacks():
    return render_template('queues_stacks.html')

@app.route('/queue-stack-algorithms')
def queue_stack_algorithms():
    return render_template('queue_stack_algorithms.html')

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@app.route('/graph-algorithms')
def graph_algorithms():
    return render_template('graph_algorithms.html')

@app.route('/dp')
def dp():
    return render_template('dp.html')

@app.route('/greedy')
def greedy():
    return render_template('greedy.html')

@app.route('/binary-search')
def binary_search():
    return render_template('binary_search.html')

@app.route('/algorithm-analysis')
def algorithm_analysis():
    return render_template('algorithm_analysis.html')

if __name__ == '__main__':
    app.run(debug=True)