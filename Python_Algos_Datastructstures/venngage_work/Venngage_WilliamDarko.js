class ShapeNode {
    constructor(xpos, ypos, height, width, hpts, vpts, dist, node_id) {
        this.x = xpos;
        this.y = ypos;
        this.height = height;
        this.width = width;
        this.dist_from_origin = dist;
        this.node_id = node_id;
        this.horizontal_points = hpts; // node's points along the x axis
        this.vertical_points = vpts; // node's points along the y axis
    }
}

/*
    Assuming the page is already populated with nodes following the class definition above
*/

const computeEuclidean = (x1,y1, x2,y2) => {
    const dist = Math.sqrt(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2));
    return dist;
}

class Grid {
    constructor(width, height) {
        this.width = width;
        this.height = height;
        this.nodes = []; // list of all nodes on the grid
        this.node_bounds_map = {}; // a mapping of node ids to node bounds information
        this.node_map = {}; // a mapping of node ids to the node object for faster lookup
        this.nodeid_to_idx = {}; // a mapping of node ids to their index in the nodes list for faster lookup
    }

    // a function to create dummy nodes for the grid
    createDummies(amount) {
        const node_width = 20; //using 20px width for dummy nodes
        for(let i = 0; i < amount; i++) {
            let xpos = Math.floor(Math.random() * (this.width - node_width) ) + node_width;
            let ypos = Math.floor(Math.random() * (this.height - node_width) ) + node_width;

            //horiz_pts[0] is the left bound of the shape, [1] is the centre, and [2] is the right bound, along the horizontal axis
            const horiz_pts = [xpos - (node_width/2), xpos, xpos + (node_width/2)];
            //vert_pts[0] is the lower bound of the shape, [1] is the centre, and [2] is the upper bound, along the vertical axis
            const vert_pts = [ypos - (node_width/2), ypos, ypos + (node_width/2)];

            const nid = i+"";
            const distance_frm_orig = computeEuclidean(0,0, xpos, ypos);

            let cur_node = new ShapeNode(xpos, ypos, node_width, node_width, horiz_pts, vert_pts, distance_frm_orig, nid);

            if(this.nodes.length == 0) {
                this.nodes.push(cur_node);
                this.nodeid_to_idx[nid] = 0;
            }
            else {
                // make sure nodes list is sorted in ascending order by distance from origin
                let idx = 0;
                while(idx < this.nodes.length && cur_node.dist_from_origin >= this.nodes[idx]['dist_from_origin']) {
                    idx++;
                }
                this.nodes.splice(idx, 0, cur_node);
                this.nodeid_to_idx[nid] = idx;
                for(let i = idx+1; i < this.nodes.length; i++) {
                    let cur_id = this.nodes[i]["node_id"];
                    this.nodeid_to_idx[cur_id]+=1; // because all the elements of the nodes list have been shifted, we update their index by 1
                }
            }
            this.node_map[nid] = cur_node;
            this.node_bounds_map[nid] = { 'h': horiz_pts, 'v': vert_pts };

        }
    }


    // drag function assumes we get the x,y coordinate of the shape after dragging it in the ui
    // first we update the node's distance from the origin, and its boundaries info
    // sencond we sort the node's list in ascending order of distance from origin
    // third we determine the closest near by nodes
    // fourth we pick an alignment

    dragNode(id, fin_x, fin_y) { // assuming we get the node id, final x position, and final y position from dragging on the UI
        // update position and bounds
        const node_width = this.node_map[id]["width"];
        this.node_map[id]["x"] = fin_x;
        this.node_map[id]["y"] = fin_y;
        this.node_map[id]["horizontal_points"] = [fin_x - (node_width/2), fin_x, fin_x + (node_width/2)];
        this.node_map[id]["vertical_points"] = [fin_y - (node_width/2), fin_y, fin_y + (node_width/2)];

        this.node_bounds_map[id]['h'] = [fin_x - (node_width/2), fin_x, fin_x + (node_width/2)];
        this.node_bounds_map[id]['v'] = [fin_y - (node_width/2), fin_y, fin_y + (node_width/2)];

        // update nodes distance from origin
        this.node_map[id]['dist_from_origin'] = computeEuclidean(0,0, fin_x,fin_y);

        // remove the node from its previous index in the nodes list
        this.nodes.splice(this.nodeid_to_idx[id],1);

        // insertion sort of updated node
        this.insertNode(this.node_map[id]);

        // because the node list is sorted by distance from the origin, for an index i,
        // the closest nodes to node at i are nodes at i-1 and i+1
        // of the two closest nodes we use the euclidean distance to get the closest of the two, which we pick for alignment.
        const nearest = this.findClosest(id);

        // given the neighbour node, we align the current node 
        this.alignNode(this.node_map[id], nearest);



    }

    insertNode(cur_node) {
        const nid = cur_node['node_id'];
        if(this.nodes.length == 0) {
            this.nodes.push(cur_node);
            this.nodeid_to_idx[nid] = 0;
        }
        else {
            // make sure nodes list is sorted in ascending order by distance from origin
            let idx = 0;
            while(idx < this.nodes.length && cur_node.dist_from_origin >= this.nodes[idx]['dist_from_origin']) {
                idx++;
            }
            this.nodes.splice(idx, 0, cur_node);
            this.nodeid_to_idx[nid] = idx;
            for(let i = idx+1; i < this.nodes.length; i++) {
                let cur_id = this.nodes[i]["node_id"];
                this.nodeid_to_idx[cur_id]+=1; // because all the elements of the nodes list have been shifted, we update their index by 1
            }
        }
    }

    findClosest(id) {
        const nidx = this.nodeid_to_idx[id];
        const left_node_idx = nidx-1;
        const right_node_idx = nidx+1;

        if(left_node_idx < 0) {
            const right_node = this.nodes[right_node_idx];
            return right_node;
        }
        if(right_node_idx >= this.nodes.length) {
            const left_node = this.nodes[left_node_idx];
            return left_node;
        }

        const cur_node = this.node_map[id];
        const right_node = this.nodes[right_node_idx];
        const left_node = this.nodes[left_node_idx];

        const left_distance = computeEuclidean(left_node.x,left_node.y, cur_node.x, cur_node.y);
        const right_distance = computeEuclidean(right_node.x, right_node.y, cur_node.x, cur_node.y);

        return left_distance < right_distance ? left_node : right_node;

    }

    alignNode(cur_node, neighbour_node) {
        // check if vertical alignment possible
        //namely if either vertical bounds, or vertical centre of the cur_node falls in the vertical bounds of neighbour node
        const neighbour_vbounds = this.node_bounds_map[neighbour_node['node_id']]['v'];
        const cur_vbounds = this.node_bounds_map[cur_node['node_id']]['v'];
        for(let bound of cur_vbounds) {
            if(bound >= neighbour_vbounds[0] && bound <= neighbour_vbounds[2]) { // if the vertical bounds of the cur node fall within that of the neighbour nodes
                // update cur_nodes new coordinates and bounds (the alingment). Either middle to middle, top to middle, top to bottom, bottom to middle, etc.
                console.log("Nodes aligned!")
                return;
            }
        }

        //check if horizontal alignment possible
        const neighbour_hbounds = this.node_bounds_map[neighbour_node['node_id']]['h'];
        const cur_hbounds = this.node_bounds_map[cur_node['node_id']]['h'];
        for(let bound of cur_hbounds) {
            if(bound >= neighbour_hbounds[0] && bound <= neighbour_hbounds[2]) { // if the vertical bounds of the cur node fall within that of the neighbour nodes
                // update cur_nodes new coordinates and bounds (the alingment). Either middle to middle, top to middle, top to bottom, bottom to middle, etc.
                console.log("Nodes aligned!")
                return;
            }
        }
        
    }


}

const main = () => {
    const shape_grid = new Grid(600, 800);
    shape_grid.createDummies(10);

    console.log(shape_grid.nodes)

    shape_grid.dragNode('0', 500, 500);

    console.log(shape_grid.nodes)
}

main();