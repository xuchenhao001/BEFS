import sys

from plot.utils.time_acc_base import plot_time_acc_attack

fed_sync_sgd = [64.87, 69.2, 69.37, 70.73, 70.4, 70.97, 70.83, 71.1, 70.83, 71.4, 71.2, 71.73, 71.3, 72.2, 72.63, 73.53, 73.9, 75.37, 75.73, 76.67, 76.43, 77.37, 77.5, 78, 78.27, 78.83, 78.7, 79.2, 79.93, 80.47, 81.13, 81.6, 81.67, 82.13, 82.27, 82.77, 82.27, 82.83, 82.77, 83.07, 82.87, 83.17, 83.2, 83.3, 83.33, 83.3, 83.5, 83.47, 83.43, 83.43, 83.53, 83.47, 83.67, 83.43, 83.57, 83.53, 83.7, 83.37, 83.7, 83.67, 83.7, 83.8, 83.77, 83.73, 83.87, 83.77, 83.97, 83.8, 84, 83.97, 83.87, 84.03, 83.9, 84.03, 84, 84.2, 84.1, 84.2, 84.13, 84.1, 84.27, 84.17, 84.27, 84.33, 84.23, 84.37, 84.4, 84.4, 84.53, 84.53, 84.43, 84.53, 84.47, 84.5, 84.5, 84.53, 84.5, 84.53, 84.5, 84.63, 84.77, 85.03, 85.1, 85.23, 85.2, 85.1, 85.27, 85.33, 85.43, 85.53, 85.57, 85.6, 85.67, 85.67, 85.67, 85.57, 85.57, 85.57, 85.63, 85.7, 85.73, 85.83, 85.77, 85.8, 85.83, 85.83, 85.97, 85.97, 86.07, 86.03, 86.13, 86.1, 86.07, 86.07, 86.17, 86.1, 86.07, 86.03, 86.13, 86.13, 86.2, 86.27, 86.27, 86.27, 86.23, 86.27, 86.37, 86.37, 86.3, 86.3, 86.3, 86.4, 86.4, 86.4, 86.4, 86.4, 86.47, 86.43, 86.43, 86.43, 86.43, 86.43, 86.43, 86.43, 86.43, 86.37, 86.37, 86.37, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.37, 86.37, 86.37, 86.37, 86.37, 86.43, 86.43, 86.43, 86.43, 86.5, 86.5, 86.5, 86.5, 86.47, 86.4, 86.4, 86.43, 86.43, 86.43, 86.43, 86.4, 86.43, 86.53, 86.53, 86.53, 86.53]
fed_avg = [14.17, 14.17, 46.73, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.6, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 62.8, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 64.03, 66.37, 66.37, 66.37, 66.37, 66.37, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 67.4, 70.03, 70.03, 72.27, 74.47, 74.47, 74.47, 74.47, 74.47, 74.47, 74.47, 74.47, 74.47, 74.47, 74.47, 74.47, 74.47, 74.47, 74.47, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 75.87, 75.87, 75.87, 75.87, 75.87, 75.87, 75.87, 75.87, 76.93, 76.93, 76.93, 76.93, 76.93, 76.9, 76.9, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.33, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.5, 77.67, 77.67, 77.67, 77.67, 77.67, 77.8, 78.5]
fed_ecsign = [46.33, 55.37, 60.9, 62.0, 65.9, 66.7, 69.33, 73.03, 73.43, 75.37, 76.37, 75.13, 77.53, 75.07, 76.87, 75.77, 77.0, 76.0, 77.93, 76.1, 78.13, 76.47, 78.47, 77.13, 78.97, 77.57, 79.37, 77.93, 79.0, 79.2, 80.83, 80.0, 82.17, 81.5, 82.5, 81.93, 81.7, 82.37, 82.83, 82.37, 82.53, 82.5, 82.4, 81.7, 82.63, 81.63, 82.23, 81.17, 83.3, 82.13, 82.7, 82.27, 83.37, 81.9, 83.63, 82.9, 84.17, 82.47, 82.9, 82.7, 83.47, 82.53, 84.0, 82.53, 83.6, 82.6, 83.63, 82.3, 83.5, 82.6, 83.87, 82.83, 83.1, 82.9, 84.4, 82.93, 84.07, 83.43, 84.5, 83.2, 84.93, 83.13, 84.33, 83.37, 85.27, 84.33, 85.0, 84.27, 85.2, 84.6, 85.23, 84.37, 84.63, 84.4, 85.57, 84.63, 85.07, 84.27, 85.67, 85.93, 86.13, 85.63, 85.83, 85.7, 85.9, 85.73, 85.8, 85.9, 85.93, 85.8, 85.9, 86.0, 85.97, 86.0, 86.0, 85.97, 85.97, 85.97, 86.0, 85.97, 85.9, 85.97, 85.93, 86.03, 86.07, 85.9, 85.97, 85.97, 85.87, 86.03, 86.13, 86.0, 86.03, 85.97, 86.0, 86.0, 86.03, 85.97, 85.9, 85.93, 86.0, 85.97, 86.0, 86.03, 85.8, 86.03, 85.97, 85.9, 85.97, 85.97, 85.9, 85.9, 85.93, 85.93, 85.93, 85.97, 86.0, 86.0, 86.0, 86.03, 85.97, 85.97, 86.0, 85.97, 86.03, 86.07, 86.03, 86.03, 86.07, 86.1, 86.07, 86.03, 86.03, 86.0, 86.03, 86.03, 86.03, 86.03, 86.0, 86.0, 86.03, 86.1, 86.07, 86.07, 86.07, 86.07, 86.07, 86.03, 86.0, 86.07, 86.03, 86.0, 86.0, 86.0, 85.97, 86.0, 86.0, 86.07, 86.07, 86.03]
fed_efsign = [48.97, 53.6, 59.6, 60.3, 60.97, 61.63, 62.87, 64.3, 65.23, 66.13, 66.6, 67.03, 67.3, 68.17, 68.97, 70.6, 71.83, 72.57, 73.5, 73.87, 74.6, 75.07, 75.47, 75.83, 76.3, 76.57, 76.83, 77.17, 77.1, 77.37, 77.43, 77.7, 77.7, 77.77, 77.8, 77.73, 78.07, 78.4, 78.13, 78.3, 78.4, 78.63, 78.27, 78.57, 78.47, 78.53, 78.53, 78.6, 78.63, 78.53, 78.6, 78.7, 78.57, 78.53, 78.7, 78.9, 78.7, 78.83, 78.7, 78.87, 78.83, 78.93, 79.03, 79.03, 79.07, 79.1, 79.13, 79.23, 79.33, 79.3, 79.3, 79.47, 79.3, 79.23, 79.23, 79.33, 79.37, 79.43, 79.4, 79.57, 79.4, 79.53, 79.53, 79.47, 79.43, 79.5, 79.5, 79.57, 79.57, 79.6, 79.5, 79.63, 79.6, 79.6, 79.63, 79.57, 79.57, 79.63, 79.63, 79.67, 79.63, 79.63, 79.57, 79.6, 79.8, 79.83, 79.7, 79.83, 79.63, 79.73, 79.87, 79.77, 79.73, 79.93, 79.6, 79.93, 79.93, 79.97, 79.73, 79.97, 80.03, 79.87, 79.8, 79.63, 80.0, 79.83, 80.03, 79.9, 80.03, 79.9, 79.93, 79.83, 80.17, 79.93, 80.03, 79.9, 80.07, 79.8, 80.2, 79.93, 79.97, 79.87, 80.17, 79.87, 80.17, 80.03, 80.13, 80.1, 80.37, 80.17, 80.4, 79.87, 80.27, 80.17, 80.23, 80.0, 80.47, 80.23, 80.3, 80.1, 80.23, 80.1, 80.57, 80.3, 80.4, 80.33, 80.5, 80.23, 80.43, 79.9, 80.6, 79.97, 80.27, 79.83, 80.33, 79.93, 80.4, 79.93, 80.47, 80.0, 80.5, 80.3, 80.67, 80.23, 80.47, 80.2, 80.4, 79.93, 80.53, 79.8, 80.43, 79.57, 80.6, 79.67, 80.7, 79.93, 80.4, 80.23, 80.13, 80.07]
fed_mvsign = [53.07, 60.2, 65.53, 66.9, 66.87, 69.57, 71.3, 74.67, 76.2, 76.37, 78.07, 76.4, 75.37, 76.93, 77.5, 77.73, 78.77, 78.5, 78.77, 78.17, 79.43, 78.6, 78.93, 79.07, 79.47, 79.87, 79.83, 80.07, 79.87, 79.47, 80.17, 80.1, 80.27, 80.17, 80.27, 80.53, 81.7, 81.77, 82.6, 81.8, 82.9, 82.93, 82.97, 83.53, 83.4, 83.6, 83.57, 83.43, 83.1, 83.67, 83.73, 83.97, 83.43, 83.77, 83.47, 83.33, 83.7, 84.4, 84.67, 83.77, 83.9, 83.83, 84.67, 83.67, 84.27, 84.17, 84.6, 83.9, 84.93, 83.97, 85.1, 83.9, 85.13, 83.87, 85.17, 82.47, 85.1, 83.47, 84.9, 83.1, 84.6, 82.87, 84.17, 83.9, 84.13, 83.5, 84.8, 83.17, 84.7, 83.27, 84.73, 83.97, 85.23, 84.57, 85.37, 83.7, 85.2, 83.6, 85.13, 85.67, 85.83, 85.77, 86.13, 86.33, 86.27, 86.17, 86.33, 86.3, 86.3, 86.27, 86.47, 86.27, 86.27, 86.17, 86.3, 86.2, 86.27, 86.3, 86.13, 86.23, 86.3, 86.23, 86.3, 86.27, 86.4, 86.33, 86.3, 86.23, 86.3, 86.43, 86.37, 86.3, 86.37, 86.37, 86.37, 86.33, 86.43, 86.47, 86.4, 86.43, 86.37, 86.37, 86.27, 86.37, 86.33, 86.4, 86.33, 86.3, 86.37, 86.37, 86.4, 86.4, 86.3, 86.33, 86.4, 86.4, 86.4, 86.43, 86.47, 86.4, 86.4, 86.4, 86.43, 86.4, 86.4, 86.4, 86.4, 86.33, 86.33, 86.33, 86.37, 86.37, 86.4, 86.47, 86.43, 86.43, 86.47, 86.47, 86.43, 86.4, 86.43, 86.37, 86.37, 86.4, 86.4, 86.4, 86.4, 86.4, 86.4, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.4, 86.43, 86.43, 86.43, 86.43]
fed_rlrsign = [46.2, 57.8, 64.73, 64.87, 65.6, 66.5, 68.4, 71.1, 72.27, 73.8, 74.57, 75.23, 75.8, 76.37, 76.67, 76.6, 76.8, 77.4, 77.77, 78.23, 78.5, 79.17, 79.2, 79.57, 80.0, 80.3, 79.83, 79.97, 80.0, 80.33, 80.6, 80.6, 80.23, 80.53, 80.73, 80.93, 80.93, 80.9, 81.0, 81.0, 81.2, 81.1, 81.33, 80.93, 81.3, 81.33, 80.9, 81.37, 81.63, 81.37, 81.37, 81.8, 81.23, 81.47, 81.7, 82.07, 81.73, 81.8, 81.63, 81.4, 81.93, 81.9, 81.77, 81.63, 82.07, 81.37, 82.13, 82.0, 82.3, 82.33, 82.37, 82.1, 82.03, 82.37, 82.6, 82.23, 82.37, 82.57, 82.6, 82.7, 82.67, 82.8, 82.37, 82.23, 82.27, 82.3, 82.43, 82.07, 82.83, 82.2, 82.57, 82.63, 82.43, 82.47, 82.43, 82.4, 82.37, 82.93, 83.03, 83.1, 83.03, 83.13, 83.17, 83.23, 83.33, 83.23, 83.3, 83.23, 83.23, 83.5, 83.23, 83.3, 83.33, 83.33, 83.33, 83.37, 83.47, 83.53, 83.53, 83.57, 83.43, 83.5, 83.5, 83.57, 83.5, 83.57, 83.5, 83.47, 83.57, 83.53, 83.6, 83.63, 83.53, 83.47, 83.47, 83.4, 83.57, 83.43, 83.4, 83.43, 83.4, 83.5, 83.4, 83.5, 83.5, 83.47, 83.37, 83.53, 83.47, 83.43, 83.43, 83.43, 83.47, 83.47, 83.43, 83.43, 83.43, 83.43, 83.4, 83.4, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43, 83.43]
fed_err = [47.27, 47.27, 47.27, 47.27, 47.27, 47.27, 47.27, 47.27, 47.27, 47.27, 47.27, 47.27, 47.27, 54.9, 54.9, 54.9, 54.9, 54.9, 54.9, 54.9, 61.7, 61.7, 61.7, 61.7, 62.2, 62.2, 62.2, 62.2, 62.2, 62.2, 62.2, 62.2, 62.2, 62.2, 62.2, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 66.7, 70.8, 72.73, 72.73, 72.73, 72.73, 72.73, 72.73, 72.73, 72.73, 72.73, 72.73, 72.73, 73.73, 73.73, 73.73, 73.73, 73.73, 75.0, 75.0, 75.0, 75.0, 75.47, 75.47, 75.47, 75.47, 75.47, 75.7, 75.7, 75.7, 75.7, 75.7, 75.7, 76.47, 76.47, 76.47, 76.47, 75.97, 75.97, 75.97, 76.63, 76.63, 76.63, 76.63, 76.63, 76.97, 76.97, 76.97, 76.97, 76.97, 76.37, 76.37, 76.37, 76.37, 76.37, 76.37, 76.37, 77.17, 77.17, 77.17, 77.57, 77.57, 78.03, 78.03, 78.03, 78.03, 78.03, 78.03, 78.03, 78.03, 78.03, 78.03, 78.03, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 77.93, 78.3, 78.3, 78.3, 78.3, 78.3, 78.3, 78.3, 78.3, 78.3, 77.77, 77.77, 77.77, 77.77, 77.77, 77.77, 77.77, 77.77, 78.03, 78.03, 78.03, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 78.27, 77.97, 77.97, 77.97, 77.97, 77.97]
fed_lfr = [13.23, 13.23, 13.23, 13.23, 13.23, 13.23, 50.93, 50.93, 62.97, 62.97, 62.97, 62.97, 62.97, 62.97, 62.97, 62.97, 62.97, 62.97, 62.97, 62.97, 62.97, 62.97, 62.97, 62.97, 62.73, 62.73, 62.73, 63.3, 63.3, 64.67, 66.93, 66.93, 66.93, 68.57, 68.57, 68.57, 68.57, 68.57, 68.57, 68.57, 68.57, 68.57, 70.13, 70.13, 70.13, 70.13, 70.13, 70.13, 70.13, 71.83, 71.83, 71.83, 73.47, 73.47, 72.93, 72.93, 72.93, 72.93, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.37, 74.37, 74.37, 74.37, 74.37, 74.37, 74.37, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.17, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 74.5, 75.13, 75.13, 75.13, 75.13, 75.13, 75.13, 75.13, 75.13, 75.13, 75.13, 75.13, 75.17, 75.17, 75.17, 75.17, 75.17, 75.17, 75.17, 75.17, 74.83, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.2, 75.6, 75.6, 75.6, 75.6, 75.6, 75.6, 75.6, 75.67, 75.67, 75.67, 75.67, 75.67, 75.67, 75.67, 75.67, 75.67, 75.67, 75.83, 75.67, 75.67, 75.67, 75.67, 75.67, 75.67]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc_attack("", fed_sync_sgd, fed_ecsign, fed_efsign, fed_mvsign, fed_rlrsign, fed_avg, fed_err, fed_lfr, save_path, plot_size="3")
