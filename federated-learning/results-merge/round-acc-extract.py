import os

from utils.parse_output import calculate_average_across_files


def extract_round_acc():
    exp_node_number = "ef"
    model_name = "mlp"
    dataset_name = "fmnist"

    experiment_names = ["fed_avg", "fed_sync", "fed_sync_sgd_1", "fed_sync_sgd_01"]
    # experiment_names = ["fed_avg", "fed_sync", "fed_sync_lrsc_5", "fed_sync_lrsc_10", "fed_sync_lrsc_20"]
    # experiment_names = ["fed_avg", "fed_sync", "fed_sync_sgd"]

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
