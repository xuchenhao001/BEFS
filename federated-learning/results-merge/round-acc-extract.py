import os

from utils.parse_output import calculate_average_across_files


def extract_round_acc():
    exp_node_number = "dynamic"
    model_name = "cnn"
    dataset_name = "cifar"

    experiment_names = ["fed_avg", "fed_sync", "fed_sync_sgd_1", "fed_sync_sgd_01", "fed_sync_sgd_001", "fed_sync_sgd_0001"]

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
