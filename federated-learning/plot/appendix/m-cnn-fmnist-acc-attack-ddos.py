import sys

from plot.utils.time_acc_base import plot_time_acc_attack

fed_sync_sgd = [24.73, 3.17, 13.67, 9.57, 16.93, 9.9, 45.13, 11.7, 46.9, 13.4, 38.43, 23.7, 42.8, 29.33, 48.3, 32.2, 56.5, 33.73, 63.57, 33.83, 69.17, 35.83, 72.37, 40.2, 74.1, 45.07, 74.97, 48.7, 74.73, 52.43, 74.87, 55.5, 74.77, 56.97, 74.97, 59.07, 75.53, 61.03, 75.93, 61.83, 76.23, 63.23, 76.73, 64.73, 77.4, 66.37, 77.7, 67.8, 78.37, 68.8, 79.03, 69.77, 79.67, 70.87, 80.13, 72.3, 80.8, 73.93, 81.57, 75.2, 81.7, 76.67, 81.7, 77.2, 82.03, 78.23, 82.7, 78.9, 82.63, 79.57, 82.97, 80.57, 83.47, 80.8, 83.63, 81.27, 83.6, 82.3, 83.9, 82.43, 83.77, 82.67, 84.03, 82.97, 84.5, 83.47, 85.23, 84.07, 85.47, 85.07, 85.77, 85.57, 86.13, 86.0, 86.7, 86.67, 87.6, 87.27, 87.4, 87.37, 87.33, 87.5, 87.73, 87.57, 87.7, 87.93, 87.87, 87.83, 88.03, 87.93, 88.07, 88.13, 88.17, 88.07, 88.1, 87.87, 87.8, 87.67, 87.73, 87.67, 87.6, 87.53, 87.83, 87.73, 87.83, 87.77, 87.87, 87.83, 87.83, 87.63, 87.6, 87.63, 87.7, 87.53, 87.47, 87.5, 87.57, 87.6, 87.5, 87.57, 87.67, 87.53, 87.57, 87.57, 87.57, 87.53, 87.67, 87.57, 87.67, 87.67, 87.63, 87.6, 87.6, 87.63, 87.63, 87.6, 87.6, 87.7, 87.7, 87.63, 87.63, 87.63, 87.67, 87.67, 87.67, 87.63, 87.67, 87.67, 87.63, 87.63, 87.53, 87.57, 87.57, 87.6, 87.6, 87.6, 87.6, 87.6, 87.57, 87.57, 87.53, 87.5, 87.5, 87.5, 87.53, 87.53, 87.5, 87.53, 87.53, 87.53, 87.53, 87.57, 87.6, 87.57, 87.57, 87.57, 87.57, 87.57, 87.57, 87.57]
fed_avg = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 79.57, 80.7, 80.7, 80.7, 80.7, 80.7, 84.43, 84.43, 83.77, 83.77, 83.77, 83.77, 83.77, 83.77, 86.87, 83.9, 83.9, 86.73, 86.73, 86.43, 87.07, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 84.43, 84.43, 84.43, 87.97, 87.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 89.57, 89.57, 89.57, 89.57, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 86.13, 88.13, 88.13, 88.13, 88.13, 88.13, 88.13, 88.13, 86.93, 86.93, 88.43, 88.43, 88.63, 88.63, 88.63, 88.4, 88.4, 88.4, 88.67, 84.63, 84.63, 84.63, 84.63, 84.63, 84.63, 84.63, 84.63, 84.63, 84.63, 84.63, 84.63, 84.63, 84.63, 84.63, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 87.3, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.9, 88.53, 88.53, 88.53]
fed_ecsign = [10.23, 34.57, 22.83, 44.7, 63.6, 33.03, 48.37, 42.3, 73.3, 59.73, 75.97, 55.67, 65.2, 57.33, 41.37, 75.47, 69.5, 84.37, 62.57, 86.43, 74.57, 74.2, 75.43, 67.3, 75.77, 79.87, 69.87, 74.47, 52.53, 68.0, 69.3, 70.83, 61.83, 72.9, 66.37, 61.33, 59.07, 63.2, 66.07, 66.07, 55.1, 67.5, 65.93, 69.83, 68.57, 65.27, 67.57, 79.5, 70.33, 77.57, 73.13, 65.67, 75.6, 79.9, 77.47, 76.13, 73.1, 74.07, 76.47, 72.53, 68.63, 78.3, 70.1, 62.8, 73.83, 71.67, 62.23, 79.17, 72.03, 54.5, 52.57, 74.57, 79.33, 50.63, 77.47, 75.37, 59.4, 70.8, 75.13, 49.67, 47.5, 82.1, 74.83, 65.07, 71.7, 71.77, 61.17, 69.03, 70.47, 68.57, 66.77, 67.93, 75.3, 72.67, 80.8, 78.4, 78.0, 78.53, 68.8, 72.27, 77.03, 80.47, 82.93, 84.2, 83.57, 84.27, 84.8, 85.2, 84.7, 84.27, 84.6, 85.07, 84.63, 85.07, 84.93, 85.1, 85.2, 85.2, 85.13, 84.9, 84.9, 84.57, 84.8, 85.03, 84.93, 85.2, 85.2, 85.47, 85.77, 85.87, 85.1, 85.17, 85.1, 84.87, 84.47, 84.73, 84.67, 84.63, 85.13, 85.1, 84.9, 84.8, 84.73, 84.6, 84.43, 84.87, 85.17, 84.83, 84.9, 84.87, 84.93, 85.07, 85.1, 85.1, 85.07, 84.97, 84.97, 84.77, 84.83, 84.83, 84.83, 84.8, 84.8, 84.73, 84.67, 84.7, 84.7, 84.67, 84.77, 84.87, 84.87, 84.9, 84.93, 84.9, 84.8, 84.83, 84.87, 84.93, 84.73, 84.87, 84.83, 84.77, 84.8, 84.83, 84.87, 84.9, 85.0, 84.9, 84.77, 84.9, 84.97, 85.1, 85.17, 85.13, 85.1, 85.07, 85.17, 84.93, 84.9, 84.93]
fed_efsign = [55.57, 60.9, 60.27, 43.43, 49.3, 40.47, 62.43, 44.57, 50.83, 39.13, 55.4, 40.5, 69.77, 74.4, 79.63, 79.6, 81.1, 79.63, 81.13, 76.0, 73.83, 61.23, 55.07, 36.7, 34.7, 23.13, 25.8, 36.57, 59.2, 70.7, 77.33, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 72.37, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 74.87, 42.37, 74.0, 74.73, 77.5, 74.5, 76.8, 69.6, 79.9, 61.47, 80.03, 76.53, 78.0, 10.0, 75.97, 80.17, 81.83, 10.0, 80.3, 72.57, 71.47, 10.0, 75.63, 79.6, 80.73, 74.6, 77.17, 82.33, 10.0, 74.8, 71.53, 71.37, 10.0, 77.5, 10.0, 76.23, 10.0, 75.8, 34.33, 71.33, 69.37, 10.0, 72.6, 80.27, 56.97, 81.63, 10.0, 54.57, 70.8, 55.97, 10.0, 76.93, 10.0, 74.3, 10.0]
fed_mvsign = [35.7, 21.63, 26.8, 33.7, 47.4, 39.53, 45.57, 36.2, 35.03, 56.0, 45.6, 58.1, 59.87, 64.5, 50.63, 72.17, 50.37, 83.6, 44.9, 81.87, 55.43, 79.37, 57.27, 68.4, 48.3, 75.8, 48.43, 72.53, 66.27, 59.3, 63.53, 74.97, 45.07, 50.3, 51.6, 67.63, 64.5, 68.73, 53.4, 54.63, 70.47, 77.77, 70.57, 64.67, 65.03, 74.13, 70.4, 76.17, 74.7, 66.07, 69.47, 77.1, 71.67, 76.4, 77.63, 69.27, 68.6, 79.1, 79.93, 76.43, 69.73, 71.23, 78.5, 77.73, 69.07, 81.57, 81.03, 67.8, 80.43, 79.23, 75.07, 78.87, 76.0, 78.7, 79.63, 78.87, 77.6, 79.8, 73.5, 77.0, 77.87, 78.37, 77.7, 81.03, 75.03, 82.3, 75.17, 82.0, 76.5, 82.17, 83.0, 86.7, 82.83, 83.53, 80.0, 85.1, 85.47, 84.77, 78.7, 82.47, 86.0, 87.73, 88.87, 88.63, 87.83, 87.7, 88.23, 88.4, 88.43, 88.43, 88.13, 88.17, 88.73, 88.9, 88.53, 88.13, 88.4, 88.43, 88.33, 88.07, 88.47, 88.27, 87.93, 88.27, 88.13, 88.0, 88.4, 87.87, 87.73, 88.07, 88.4, 87.87, 88.4, 87.97, 88.33, 87.37, 88.1, 87.83, 88.37, 87.77, 87.9, 87.73, 88.1, 87.93, 86.93, 86.77, 88.23, 88.83, 88.33, 88.3, 88.33, 88.17, 88.03, 88.13, 88.4, 88.4, 88.43, 88.23, 88.33, 88.3, 88.4, 88.37, 88.33, 88.23, 88.23, 88.27, 88.3, 88.33, 88.3, 88.33, 88.37, 88.37, 88.37, 88.47, 88.57, 88.47, 88.47, 88.4, 88.43, 88.37, 88.47, 88.43, 88.47, 88.53, 88.57, 88.57, 88.6, 88.63, 88.53, 88.53, 88.53, 88.5, 88.43, 88.5, 88.57, 88.6, 88.6, 88.47, 88.53, 88.53]
fed_rlrsign = [18.4, 27.8, 22.93, 26.6, 54.53, 68.27, 65.27, 67.2, 64.0, 68.63, 58.57, 64.3, 66.3, 59.07, 64.07, 75.63, 69.27, 74.57, 74.87, 70.93, 64.73, 69.9, 71.9, 73.37, 69.03, 67.07, 68.23, 67.87, 65.33, 67.33, 65.23, 66.3, 68.3, 73.53, 67.2, 76.43, 73.57, 76.7, 77.2, 75.5, 78.5, 78.5, 79.5, 79.67, 77.27, 76.8, 79.37, 78.77, 75.7, 78.47, 80.2, 79.57, 79.6, 79.47, 78.53, 76.3, 79.17, 79.1, 77.6, 74.0, 77.43, 78.17, 75.87, 77.67, 78.37, 79.07, 78.97, 78.9, 78.67, 78.77, 78.0, 78.47, 75.07, 74.9, 73.9, 75.43, 77.47, 77.9, 75.3, 72.37, 68.37, 67.33, 68.27, 67.5, 65.97, 60.17, 58.0, 59.17, 58.67, 52.67, 54.03, 51.47, 52.6, 48.57, 39.77, 35.93, 38.7, 40.27, 38.2, 38.3, 38.83, 39.13, 39.57, 39.63, 39.87, 39.53, 38.73, 38.8, 38.53, 38.27, 38.9, 38.53, 38.57, 38.9, 38.03, 37.9, 38.33, 38.4, 38.87, 39.03, 39.07, 39.37, 39.3, 39.83, 39.63, 39.7, 39.8, 40.0, 40.23, 39.83, 39.4, 39.57, 39.87, 39.87, 40.07, 40.23, 39.43, 39.7, 39.93, 40.0, 40.57, 40.6, 40.3, 40.23, 40.53, 40.43, 40.63, 40.87, 41.33, 41.4, 41.5, 41.43, 41.5, 41.47, 41.4, 41.43, 41.23, 41.4, 41.43, 41.4, 41.33, 41.33, 41.53, 41.4, 41.4, 41.33, 41.33, 41.3, 41.33, 41.33, 41.33, 41.27, 41.27, 41.27, 41.27, 41.23, 41.27, 41.33, 41.3, 41.3, 41.33, 41.3, 41.27, 41.23, 41.2, 41.23, 41.23, 41.27, 41.27, 41.27, 41.2, 41.2, 41.2, 41.2, 41.2, 41.2, 41.2, 41.1, 41.1, 41.2]
fed_err = [10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 10.63, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 83.83, 83.83, 83.83, 83.37, 83.37, 83.37, 83.37, 83.37, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 85.3, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 86.97, 79.77, 79.77, 79.77, 79.77, 79.77, 79.77, 79.77, 79.77, 79.77, 79.77, 79.77, 79.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.77, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 86.33, 87.57, 87.57, 87.57, 87.57, 87.93, 87.93, 87.93, 87.93]
fed_lfr = [10.0, 81.17, 81.17, 82.87, 82.87, 82.87, 82.87, 82.87, 82.87, 82.87, 82.87, 82.87, 82.87, 82.87, 82.87, 82.87, 82.87, 78.63, 78.63, 78.63, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 84.3, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 83.03, 86.3, 86.3, 86.3, 86.3, 86.3, 86.3, 87.43, 87.43, 87.43, 87.43, 87.43, 87.43, 87.43, 87.43, 87.43, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 86.37, 87.9, 87.9, 87.9, 87.9, 87.9, 87.9, 87.9, 87.9, 87.9, 87.9, 87.9, 87.9, 87.9, 87.9, 87.9, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.13, 87.57, 87.57, 87.57, 87.57, 87.57, 87.57, 87.57, 87.57, 87.57, 87.57, 87.57, 87.57, 87.57, 86.63, 87.63, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 87.03, 86.9, 86.9, 86.9, 86.9, 86.9, 86.9, 86.9, 86.9, 88.77, 88.77, 88.77, 88.77, 88.77, 88.77, 88.77]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc_attack("", fed_sync_sgd, fed_ecsign, fed_efsign, fed_mvsign, fed_rlrsign, fed_avg, fed_err, fed_lfr, False, False, save_path, plot_size="3")