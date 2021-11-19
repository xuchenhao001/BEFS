import sys

from plot.utils.time_acc_base import plot_time_acc_attack

fed_sync_sgd = [40.83, 9.2, 45.07, 26.6, 58.8, 44.43, 60.7, 46.2, 66.47, 46.63, 68.37, 46.13, 64.23, 45.43, 60.1, 48.4, 59.43, 52.5, 57.3, 50.1, 55.97, 48.63, 54.5, 46.7, 53.53, 43.8, 50.8, 43.87, 48.93, 44.13, 47.83, 43.9, 47.17, 44.87, 47.47, 45.97, 46.2, 45.5, 44.4, 42.83, 42.9, 41.6, 41.43, 42.53, 42.23, 42.8, 40.9, 42.9, 41.2, 43.43, 41.1, 42.0, 40.53, 42.77, 40.73, 46.2, 42.57, 46.5, 43.4, 48.0, 43.43, 48.4, 44.57, 51.77, 47.23, 54.47, 51.1, 56.73, 54.3, 58.23, 56.97, 58.5, 57.67, 59.53, 61.27, 61.83, 63.7, 63.47, 66.3, 64.57, 68.4, 66.23, 70.47, 68.03, 72.1, 70.43, 74.57, 73.17, 76.93, 77.03, 79.37, 80.3, 83.07, 83.17, 84.83, 85.43, 86.5, 87.47, 88.3, 88.27, 88.27, 88.2, 88.3, 88.27, 88.47, 88.63, 88.7, 88.67, 88.53, 88.53, 88.4, 88.4, 88.4, 88.47, 88.53, 88.37, 88.53, 88.33, 88.37, 88.27, 88.67, 88.53, 88.4, 88.37, 88.43, 88.47, 88.67, 88.5, 88.6, 88.47, 88.53, 88.5, 88.43, 88.43, 88.43, 88.5, 88.33, 88.47, 88.27, 88.07, 88.4, 88.27, 88.43, 88.17, 88.2, 88.13, 88.13, 88.23, 88.4, 88.4, 88.33, 88.37, 88.4, 88.33, 88.33, 88.33, 88.3, 88.33, 88.37, 88.37, 88.37, 88.33, 88.3, 88.3, 88.37, 88.33, 88.37, 88.33, 88.33, 88.27, 88.27, 88.27, 88.27, 88.27, 88.27, 88.27, 88.23, 88.23, 88.27, 88.27, 88.3, 88.3, 88.3, 88.27, 88.27, 88.27, 88.27, 88.27, 88.3, 88.3, 88.3, 88.43, 88.4, 88.47, 88.47, 88.47, 88.47, 88.5, 88.53, 88.5]
fed_avg = [83.77, 82.17, 87.03, 85.53, 82.97, 86.17, 86.33, 85.13, 87.37, 85.9, 87.53, 87.67, 85.3, 85.37, 86.7, 85.57, 84.5, 87.43, 86.97, 85.57, 87.07, 83.53, 87.33, 85.0, 87.27, 86.47, 86.8, 87.07, 86.97, 87.33, 86.77, 87.53, 86.93, 87.17, 85.77, 85.47, 87.4, 88.1, 87.4, 86.6, 87.57, 75.67, 84.0, 86.87, 86.07, 85.9, 86.13, 87.0, 85.93, 85.6, 86.67, 86.0, 85.63, 85.73, 82.83, 86.7, 83.8, 85.9, 87.53, 86.2, 86.43, 81.5, 87.0, 86.63, 80.37, 84.27, 84.63, 85.07, 86.2, 86.3, 79.93, 86.8, 87.1, 86.2, 86.2, 84.87, 85.37, 87.13, 86.7, 86.2, 84.07, 87.27, 84.53, 86.13, 84.33, 86.23, 80.83, 86.5, 83.93, 85.5, 85.73, 84.5, 85.8, 83.9, 10.0, 86.33, 83.63, 86.63, 84.03, 83.87, 86.63, 84.6, 86.77, 86.23, 85.73, 86.03, 88.37, 85.63, 85.3, 85.8, 84.3, 83.87, 83.97, 86.3, 80.33, 85.07, 86.57, 86.43, 86.83, 87.0, 86.27, 86.4, 84.9, 84.67, 86.17, 86.77, 86.27, 86.4, 84.23, 84.67, 87.1, 84.93, 86.27, 83.87, 86.5, 87.03, 86.9, 86.8, 86.57, 85.2, 86.03, 86.37, 86.3, 87.77, 85.83, 82.7, 87.1, 81.37, 83.7, 86.03, 86.73, 86.03, 84.0, 87.23, 85.8, 85.6, 86.13, 82.6, 84.23, 86.97, 86.67, 87.0, 87.27, 77.2, 86.63, 87.37, 86.63, 83.33, 82.9, 84.13, 86.13, 85.53, 86.87, 84.07, 87.13, 85.8, 84.37, 84.4, 79.4, 85.3, 85.47, 84.57, 83.4, 87.2, 86.9, 85.07, 86.33, 85.07, 85.57, 85.73, 83.0, 86.8, 86.8, 64.17, 86.03, 87.33, 86.4, 80.4, 87.2, 85.33]
fed_ecsign = [17.33, 42.9, 52.33, 52.03, 71.93, 53.63, 65.2, 57.63, 67.9, 53.17, 61.13, 32.47, 37.33, 40.97, 47.7, 46.0, 46.87, 44.8, 49.7, 33.33, 41.17, 25.27, 30.87, 32.83, 35.93, 20.7, 28.7, 11.37, 18.13, 10.7, 11.7, 12.3, 10.37, 10.27, 11.4, 10.0, 14.2, 10.57, 16.23, 10.1, 10.67, 10.23, 10.0, 10.47, 10.03, 10.03, 10.1, 10.03, 10.0, 10.1, 10.13, 10.53, 11.6, 18.53, 10.23, 13.2, 10.1, 12.33, 10.97, 10.2, 12.53, 10.07, 10.87, 19.2, 10.07, 18.87, 25.9, 10.07, 26.67, 10.23, 17.17, 10.93, 21.4, 21.3, 25.83, 33.9, 16.27, 38.2, 31.17, 30.47, 44.97, 10.7, 44.67, 40.8, 52.7, 45.77, 51.53, 28.0, 53.73, 62.67, 36.73, 67.0, 49.0, 71.9, 58.47, 64.03, 66.93, 65.4, 72.33, 75.53, 79.97, 84.27, 85.6, 84.47, 83.0, 83.33, 84.57, 85.03, 85.17, 85.07, 85.4, 85.3, 85.4, 85.77, 85.6, 85.4, 84.27, 85.7, 85.67, 85.57, 85.13, 85.37, 85.5, 85.4, 85.53, 85.27, 85.0, 85.53, 85.5, 85.37, 85.27, 85.43, 85.3, 85.2, 85.63, 85.53, 85.67, 85.47, 85.97, 85.63, 85.43, 85.8, 84.57, 85.77, 86.0, 85.37, 85.5, 85.2, 85.23, 85.27, 85.4, 85.43, 85.5, 85.67, 85.57, 85.5, 85.53, 85.53, 85.57, 85.8, 85.8, 85.83, 85.83, 85.87, 85.97, 85.77, 85.67, 85.43, 85.4, 85.53, 85.57, 85.53, 85.57, 85.5, 85.5, 85.5, 85.5, 85.47, 85.47, 85.5, 85.53, 85.6, 85.5, 85.57, 85.53, 85.53, 85.53, 85.5, 85.5, 85.57, 85.6, 85.53, 85.5, 85.37, 85.43, 85.43, 85.47, 85.53, 85.5, 85.6]
fed_efsign = [65.37, 66.33, 73.5, 73.33, 71.0, 75.1, 70.67, 76.87, 72.5, 77.77, 69.17, 74.57, 71.73, 68.07, 61.33, 64.13, 61.4, 45.8, 54.07, 39.4, 48.73, 44.23, 50.33, 39.17, 53.83, 38.2, 68.6, 54.87, 73.43, 47.83, 74.67, 56.17, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 46.83, 10.5, 27.23, 18.0, 19.33, 10.1, 11.07, 10.0, 10.3, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 20.47, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
fed_mvsign = [10.0, 9.57, 30.53, 37.93, 40.4, 44.03, 45.97, 39.3, 44.57, 43.5, 38.0, 41.07, 40.07, 25.4, 52.33, 45.5, 44.77, 42.57, 46.83, 37.1, 36.93, 40.33, 24.67, 30.53, 30.07, 26.23, 27.63, 28.13, 18.03, 25.53, 11.2, 18.37, 10.63, 13.97, 10.63, 10.3, 10.1, 10.03, 10.0, 10.0, 10.03, 10.0, 10.0, 10.0, 10.0, 10.0, 11.67, 10.0, 10.07, 10.0, 10.0, 11.8, 10.0, 17.37, 10.9, 25.9, 23.2, 19.67, 31.63, 33.93, 27.67, 23.5, 39.9, 21.27, 37.23, 31.8, 47.17, 33.57, 43.0, 53.77, 37.77, 59.9, 49.67, 62.0, 43.1, 63.07, 34.63, 59.9, 54.67, 45.1, 56.9, 50.0, 43.8, 46.43, 57.73, 46.27, 41.67, 41.23, 62.5, 47.47, 70.3, 58.17, 64.47, 61.27, 60.63, 61.77, 71.07, 71.47, 71.4, 76.07, 79.5, 81.63, 82.9, 82.8, 82.43, 81.9, 81.9, 82.17, 81.2, 82.27, 82.4, 82.4, 82.2, 81.83, 81.9, 81.8, 82.57, 82.5, 80.3, 82.0, 82.57, 82.57, 82.63, 82.6, 81.77, 81.97, 82.6, 82.23, 82.13, 82.2, 80.6, 82.47, 82.53, 83.23, 82.33, 82.47, 82.33, 82.23, 82.6, 82.0, 80.4, 82.43, 82.6, 82.33, 82.4, 82.53, 82.37, 81.83, 82.33, 82.37, 82.4, 82.33, 82.43, 82.37, 82.43, 82.57, 82.6, 82.6, 82.73, 82.73, 82.63, 82.7, 82.87, 82.83, 82.73, 82.73, 82.77, 82.73, 82.77, 82.77, 82.8, 82.63, 82.73, 82.83, 82.77, 82.83, 83.0, 82.93, 82.8, 82.97, 83.0, 82.93, 82.87, 83.03, 83.1, 83.07, 83.03, 82.97, 82.97, 82.97, 83.0, 83.0, 82.97, 83.1, 83.1, 83.1, 83.0, 83.1, 83.03, 83.0]
fed_rlrsign = [46.97, 47.43, 33.57, 26.5, 30.73, 29.43, 31.47, 12.47, 10.0, 10.0, 8.5, 11.33, 10.03, 17.57, 19.7, 36.4, 35.1, 23.33, 20.3, 23.53, 15.37, 24.83, 20.3, 19.3, 21.8, 10.1, 35.2, 25.93, 24.6, 27.73, 31.0, 28.9, 37.63, 21.23, 21.33, 39.5, 39.97, 36.77, 41.5, 34.6, 31.93, 34.57, 24.5, 18.1, 22.8, 30.73, 21.37, 22.07, 38.27, 40.2, 30.83, 24.87, 23.77, 28.4, 33.37, 26.8, 32.23, 22.67, 22.77, 18.97, 24.87, 17.87, 21.37, 28.77, 24.43, 19.9, 29.77, 17.9, 17.93, 19.77, 21.63, 20.77, 21.8, 24.8, 30.27, 39.8, 35.57, 25.83, 28.6, 25.3, 26.4, 30.83, 35.9, 38.97, 32.13, 34.27, 38.0, 31.2, 27.57, 33.3, 43.73, 38.23, 35.63, 31.2, 28.07, 36.33, 46.0, 51.4, 55.77, 56.03, 55.73, 57.03, 57.93, 59.17, 59.1, 57.5, 57.73, 57.13, 58.43, 57.83, 57.1, 55.0, 31.53, 54.43, 56.8, 57.1, 57.13, 58.5, 57.2, 55.5, 57.37, 58.0, 57.0, 56.63, 55.8, 54.8, 53.73, 55.0, 55.6, 55.97, 55.83, 53.8, 31.5, 53.83, 52.17, 54.03, 54.13, 54.63, 54.57, 52.4, 22.77, 10.0, 10.0, 10.0, 10.0, 10.0, 22.3, 36.33, 48.63, 49.37, 49.8, 49.03, 49.8, 50.27, 50.6, 51.3, 51.07, 51.23, 50.77, 51.33, 51.6, 51.37, 51.0, 51.03, 51.47, 51.97, 52.5, 53.07, 53.23, 53.57, 53.83, 53.87, 53.77, 53.53, 53.5, 53.4, 53.2, 53.03, 52.77, 52.63, 52.8, 52.8, 52.83, 52.87, 52.43, 51.7, 51.47, 50.5, 49.9, 50.23, 50.63, 50.07, 50.73, 50.57, 51.17, 50.9, 50.93, 51.5, 52.17, 52.97]
fed_err = [85.1, 87.7, 87.93, 87.3, 89.0, 88.37, 88.97, 89.23, 88.83, 89.0, 89.13, 89.07, 89.0, 89.13, 88.97, 89.03, 88.93, 88.93, 88.87, 88.9, 88.7, 89.1, 89.03, 88.93, 88.67, 88.53, 88.63, 88.93, 88.9, 88.73, 88.8, 88.67, 88.7, 88.93, 88.87, 88.83, 88.73, 88.8, 88.9, 88.87, 88.87, 88.77, 88.67, 88.83, 88.93, 88.73, 88.67, 88.67, 88.5, 88.77, 88.73, 88.8, 88.37, 88.5, 88.53, 88.43, 88.33, 88.43, 88.6, 88.43, 88.47, 88.43, 88.57, 88.5, 88.53, 88.33, 88.27, 88.3, 88.3, 88.4, 88.73, 88.7, 88.57, 88.57, 88.5, 88.47, 88.4, 88.5, 88.43, 88.33, 88.33, 88.43, 88.33, 88.33, 88.27, 88.33, 88.33, 88.27, 88.27, 88.27, 88.23, 88.27, 88.27, 88.27, 88.3, 88.27, 88.33, 88.37, 88.23, 88.33, 88.27, 88.23, 88.27, 88.3, 88.33, 88.37, 88.3, 88.33, 88.43, 88.33, 88.23, 88.3, 88.3, 88.33, 88.3, 88.27, 88.3, 88.33, 88.27, 88.3, 88.2, 88.37, 88.2, 88.2, 88.2, 88.3, 88.2, 88.27, 88.23, 88.23, 88.23, 88.2, 88.27, 88.3, 88.3, 88.2, 88.2, 88.23, 88.23, 88.23, 88.23, 88.13, 88.2, 88.23, 88.2, 88.57, 88.5, 88.63, 88.63, 88.63, 88.53, 88.57, 88.43, 88.53, 88.53, 88.6, 88.6, 88.57, 88.53, 88.53, 88.5, 88.53, 88.5, 88.5, 88.53, 88.43, 88.43, 88.4, 88.4, 88.33, 88.4, 88.43, 88.4, 88.53, 88.33, 88.3, 88.33, 88.37, 88.43, 88.43, 88.4, 88.33, 88.3, 88.33, 88.33, 88.37, 88.47, 88.33, 88.37, 88.37, 88.33, 88.43, 88.37, 88.33, 88.37, 88.37, 88.37, 88.37, 88.33, 88.37]
fed_lfr = [84.0, 85.87, 86.57, 86.53, 86.37, 86.93, 86.73, 87.13, 87.23, 86.93, 86.1, 81.67, 84.63, 82.03, 86.9, 63.47, 84.9, 84.27, 81.8, 85.83, 65.93, 81.97, 74.9, 86.03, 85.13, 85.73, 82.47, 79.27, 85.93, 87.43, 86.43, 85.9, 86.63, 87.47, 49.67, 76.33, 85.87, 86.87, 83.2, 74.93, 83.27, 86.0, 86.33, 83.6, 83.2, 86.9, 86.27, 86.83, 85.97, 86.37, 86.4, 85.47, 86.0, 86.5, 87.2, 87.77, 84.4, 86.47, 87.4, 86.8, 87.2, 87.0, 87.3, 50.57, 86.07, 84.47, 71.87, 84.77, 85.93, 64.43, 83.6, 86.33, 86.97, 83.07, 87.43, 83.73, 87.17, 86.47, 86.43, 86.97, 85.77, 85.03, 86.3, 84.57, 87.6, 10.0, 85.23, 86.3, 86.83, 85.13, 86.7, 85.27, 79.07, 86.83, 87.7, 86.77, 87.07, 87.2, 83.2, 86.67, 85.53, 86.07, 86.2, 87.63, 86.47, 84.97, 86.2, 87.53, 87.03, 87.43, 86.9, 87.13, 86.07, 87.07, 86.23, 86.23, 87.47, 85.6, 87.1, 10.0, 86.1, 28.47, 86.03, 85.7, 86.7, 86.83, 80.73, 86.63, 84.2, 86.17, 85.87, 86.4, 86.87, 87.43, 86.9, 69.3, 79.33, 86.73, 87.0, 86.93, 85.4, 86.5, 75.5, 86.0, 86.5, 86.17, 86.97, 86.63, 86.6, 87.43, 86.6, 85.77, 75.43, 87.03, 78.53, 86.8, 86.57, 84.77, 87.0, 83.3, 86.3, 86.8, 85.67, 85.97, 87.3, 86.87, 87.23, 86.57, 86.27, 85.23, 73.93, 85.8, 87.17, 86.5, 87.23, 84.67, 87.13, 84.23, 86.5, 87.03, 87.13, 87.27, 86.6, 86.8, 87.17, 77.07, 69.6, 85.8, 86.93, 81.53, 86.17, 85.5, 85.13, 87.0, 79.07, 86.47, 66.17, 86.2, 86.87, 84.63]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc_attack("", fed_sync_sgd, fed_ecsign, fed_efsign, fed_mvsign, fed_rlrsign, fed_avg, fed_err, fed_lfr, save_path, plot_size="3")
