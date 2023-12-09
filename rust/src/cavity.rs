use graph::prelude::*;
use csv::Writer;
use crate::utils::*;

pub fn original_cavity(G: &UndirectedCsrGraph<usize>, trans: &Vec<f32>) -> Vec<Vec<f32>> {
    // Returns estimated node risk for each node in G
    let (edge_list, hashimoto) = create_hashimoto(&G);
    let mut risk_list = Vec::new();

    for T in trans.iter() {
        let mut risk = vec![1.0; G.node_count()];
        let mut intermediate_risk = vec![1.0; hashimoto.node_count() as usize];

        // Calculate intermediate risks
        let iterations = 100;
        for _ in 0..iterations {
            for i in 0..hashimoto.node_count() {
                let mut new_value: f32 = 1.0;
                for t in hashimoto.out_neighbors_with_values(i as u32){
                    new_value *= (1.0 - T * intermediate_risk[t.target as usize]); 
                }
                new_value = 1.0 - new_value;
                for t in hashimoto.in_neighbors_with_values(i as u32){
                    intermediate_risk[t.target as usize] = new_value;
                }

            }
        }

        // Calculate final risk
        for (idx, edge) in edge_list.iter().enumerate() {
            let (i, j) = edge;
            risk[*i] *= (1.0 - T * intermediate_risk[idx]);
        }
        for i in 0..risk.len() {
            risk[i] = 1.0 - risk[i];
        }
        risk_list.push(risk);
    }
    // Write node risks to file
    let file_path = "/home/mbowditch/Documents/cavity_method/code/python/data/output_cavity.csv";
    let mut writer = Writer::from_path(file_path).unwrap();

    // Write tuples to the CSV file
    for t in 0..trans.len() {
        let string_risk: Vec<String> = risk_list[t].iter().map(|&x| x.to_string()).collect();
        writer.write_record(string_risk).unwrap();
    }

    // Close the CSV file
    writer.flush().unwrap();
    risk_list
}
