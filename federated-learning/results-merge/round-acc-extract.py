import os

from utils.parse_output import calculate_average_across_files


def extract_round_acc():
    exp_node_number = "attack"
    model_name = "mlp"
    dataset_name = "fmnist"

    # experiment_names = ["fed_avg", "fed_efsign", "fed_sign", "fed_sync", "fed_sync_sgd", "local_train"]
    # experiment_names = ["fed_avg", "fed_ecsign", "fed_efsign", "fed_mvsign", "fed_rlrsign", "fed_sync_sgd"]
    # experiment_names = ["fed_avg_ddos095", "fed_ecsign_ddos095", "fed_efsign_ddos095", "fed_mvsign_ddos095", "fed_rlrsign_ddos095", "fed_sync_sgd_ddos095"]
    # experiment_names = ["fed_avg_ddos099", "fed_ecsign_ddos099", "fed_efsign_ddos099", "fed_mvsign_ddos099", "fed_rlrsign_ddos099", "fed_sync_sgd_ddos099"]
    experiment_names = ["fed_rlrsign_ddos095", "fed_rlrsign_ddos099", "fed_rlrsign_poisoning", "fed_rlrsign_trojan"]

    for path, dirs, files in os.walk("./output"):
        if path.endswith(model_name + "-" + dataset_name) and exp_node_number in path:
            for experiment_name in experiment_names:
                experiment_path = os.path.join(path, experiment_name)
                files_numbers_mean_2d_np = calculate_average_across_files(experiment_path)
                acc = [round(i, 2) for i in files_numbers_mean_2d_np[:, 5]]
                print(experiment_name, "=", acc)


def main():
    extract_round_acc()


if __name__ == "__main__":
    main()
