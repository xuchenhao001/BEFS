import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [53.97, 57.51, 65.65, 66.32, 66.78, 66.86, 66.86, 66.59, 67.22, 67.35, 67.27, 66.81, 67.08, 67.32, 67.41, 67.59, 67.59, 67.62, 67.46, 67.57, 67.49, 67.32, 67.46, 67.54, 67.46, 67.3, 67.32, 67.27, 67.38, 67.43, 67.22, 67.03, 66.89, 66.97, 67.3, 67.43, 67.68, 67.51, 67.76, 67.65, 67.57, 67.24, 67.14, 67.08, 66.76, 67.05, 67.08, 67.3, 67.73, 67.51, 67.38, 67.59, 67.51, 67.84, 67.51, 67.49, 67.27, 67.62, 67.65, 67.62, 67.78, 67.97, 67.76, 67.81, 67.97, 67.62, 67.54, 67.46, 67.89, 67.73, 67.7, 67.81, 67.62, 67.46, 66.95, 67.43, 67.73, 67.81, 67.81, 67.65, 67.78, 67.43, 67.43, 67.35, 67.68, 67.65, 67.41, 67.38, 67.19, 67.24, 67.08, 66.89, 67.62, 67.54, 67.65, 67.41, 67.46, 67.46, 67.68, 68.19, 67.81, 68.16, 68.0, 67.84, 67.59, 67.57, 67.38, 67.32, 67.84, 67.7, 67.76, 67.54, 67.49, 67.68, 67.86, 67.7, 67.97, 67.54, 67.89, 68.03, 68.11, 68.14, 67.97, 68.14, 67.95, 67.68, 67.3, 67.51, 67.7, 67.84, 67.84, 67.84, 67.95, 67.92, 67.92, 67.59, 67.86, 67.76, 67.57, 67.86, 67.73, 67.95, 67.84, 67.43, 67.7, 67.41, 67.57, 67.41, 67.57, 67.59, 67.3, 67.35, 67.3, 67.41, 67.51, 67.57, 67.54, 67.76, 67.57, 66.95, 67.38, 67.51, 67.38, 67.97, 67.89, 68.14, 68.22, 67.76, 68.0, 67.78, 67.92, 67.84, 67.84, 67.89, 67.81, 67.89, 68.0, 67.78, 67.65, 67.73, 67.89, 68.03, 68.05, 68.16, 67.7, 68.03, 67.95, 68.0, 68.16, 67.7, 67.59, 67.78, 67.59, 67.76, 67.86, 67.65, 67.65, 67.89, 67.84, 67.84]
fed_efsign = [42.16, 46.86, 12.16, 59.46, 61.32, 50.62, 43.32, 33.38, 61.81, 25.65, 61.27, 61.62, 4.49, 20.0, 65.38, 2.62, 0.41, 58.27, 12.92, 9.24, 16.76, 23.3, 4.19, 17.14, 26.65, 19.46, 45.14, 20.03, 56.11, 57.7, 9.35, 9.22, 48.32, 8.76, 21.73, 38.43, 46.59, 7.59, 19.14, 16.68, 60.16, 14.78, 28.78, 10.0, 17.05, 54.24, 0.43, 53.46, 58.03, 43.97, 15.0, 61.38, 5.95, 0.81, 61.16, 7.35, 9.11, 10.38, 46.27, 14.19, 24.16, 54.43, 39.81, 18.59, 9.89, 10.0, 48.16, 8.49, 7.41, 57.73, 64.57, 22.54, 0.16, 56.78, 0.16, 40.46, 7.86, 16.95, 10.0, 56.38, 0.73, 8.03, 59.7, 58.54, 9.59, 4.38, 35.51, 43.51, 34.3, 14.27, 7.14, 4.76, 10.7, 31.03, 33.35, 8.62, 0.49, 12.08, 22.32, 48.76, 0.19, 0.86, 37.14, 23.81, 7.49, 16.27, 47.46, 21.73, 17.78, 28.08, 10.27, 23.41, 50.68, 32.08, 11.03, 22.19, 47.68, 15.24, 13.41, 2.7, 13.3, 4.38, 15.97, 7.32, 13.81, 13.0, 27.78, 9.92, 9.14, 11.73, 34.84, 2.84, 6.38, 8.16, 12.65, 10.76, 12.32, 10.0, 9.0, 32.16, 6.95, 6.49, 9.95, 10.11, 37.11, 18.84, 21.19, 30.73, 1.73, 10.0, 30.7, 10.0, 13.19, 17.51, 14.22, 17.41, 16.57, 10.14, 10.05, 44.46, 5.16, 16.08, 9.84, 11.16, 16.11, 14.14, 17.16, 14.35, 12.89, 14.46, 17.7, 13.49, 11.11, 3.38, 7.14, 11.46, 9.57, 5.68, 24.16, 7.65, 4.92, 3.27, 9.62, 16.03, 11.19, 10.57, 10.22, 11.16, 15.57, 9.43, 8.43, 10.46, 7.22, 11.27, 9.68, 10.16, 10.14, 6.41, 7.22, 8.76]
fed_sync = [37.62, 47.62, 53.89, 62.41, 64.59, 65.24, 65.35, 66.14, 66.81, 66.38, 66.27, 67.0, 67.05, 67.46, 67.7, 67.65, 67.46, 67.32, 67.51, 67.0, 67.54, 67.38, 67.57, 67.92, 67.81, 67.41, 67.62, 67.84, 67.65, 67.41, 67.92, 67.76, 67.92, 67.78, 67.84, 67.89, 68.49, 68.59, 68.38, 67.89, 68.54, 68.89, 68.62, 68.46, 67.97, 68.27, 67.65, 67.86, 68.19, 68.3, 68.24, 68.41, 68.68, 68.51, 68.19, 68.08, 68.41, 68.11, 68.46, 68.08, 68.43, 68.49, 68.41, 68.41, 67.92, 67.95, 67.95, 67.14, 67.49, 67.73, 67.7, 67.73, 68.22, 68.24, 68.22, 68.05, 68.14, 68.0, 68.19, 68.05, 67.59, 68.03, 68.05, 68.38, 68.7, 68.43, 68.49, 68.19, 67.78, 67.51, 67.16, 67.59, 67.0, 67.41, 66.86, 67.46, 67.89, 67.68, 67.59, 67.68, 68.16, 68.08, 68.16, 68.16, 67.89, 67.84, 67.97, 67.89, 68.49, 68.32, 67.89, 67.73, 67.68, 68.27, 68.35, 68.16, 67.78, 68.22, 68.0, 67.7, 68.22, 68.24, 68.05, 68.38, 68.65, 68.32, 68.0, 68.43, 68.24, 68.16, 68.08, 67.95, 68.19, 68.08, 68.16, 67.92, 68.35, 67.81, 68.11, 68.22, 68.32, 68.46, 68.3, 68.32, 68.14, 68.68, 68.57, 68.68, 68.38, 68.41, 68.14, 67.81, 67.84, 67.32, 67.95, 68.05, 68.19, 68.22, 68.22, 67.97, 67.84, 67.78, 67.81, 67.81, 67.65, 67.95, 67.62, 68.14, 67.49, 68.16, 67.73, 68.27, 68.43, 68.35, 68.0, 67.59, 68.14, 68.03, 67.86, 67.95, 68.35, 68.22, 68.35, 68.22, 68.08, 67.92, 67.54, 67.84, 67.3, 67.41, 67.62, 67.11, 67.62, 67.41, 67.73, 68.19, 68.11, 68.3, 68.41, 67.73]
fed_sync_sgd = [53.65, 61.0, 59.7, 63.73, 62.65, 65.51, 65.38, 65.76, 66.22, 65.97, 66.81, 66.19, 67.35, 66.65, 67.78, 67.78, 68.86, 69.35, 69.86, 70.49, 70.76, 71.24, 71.76, 72.35, 72.32, 72.97, 72.97, 73.89, 73.89, 74.59, 74.73, 75.16, 74.92, 75.54, 75.27, 75.92, 75.81, 76.38, 76.24, 76.49, 76.3, 76.59, 76.46, 76.92, 76.78, 77.05, 77.11, 77.41, 77.05, 77.57, 76.95, 77.46, 77.19, 77.57, 77.32, 77.62, 77.41, 77.7, 77.62, 77.73, 77.78, 77.92, 77.76, 77.92, 77.73, 78.03, 77.68, 77.95, 77.7, 78.05, 78.0, 78.19, 78.05, 78.32, 78.05, 78.32, 78.14, 78.35, 78.22, 78.41, 78.32, 78.43, 78.3, 78.59, 78.35, 78.38, 78.16, 78.41, 78.35, 78.46, 78.3, 78.57, 78.38, 78.68, 78.54, 78.68, 78.59, 78.73, 78.57, 78.51, 78.62, 78.59, 78.65, 78.76, 78.89, 78.92, 78.97, 79.0, 79.05, 79.11, 79.11, 79.05, 79.0, 78.97, 78.97, 78.97, 78.92, 78.97, 78.95, 78.95, 78.97, 78.95, 78.92, 78.97, 78.97, 79.0, 79.03, 79.0, 79.03, 79.0, 79.05, 78.97, 79.05, 78.97, 79.08, 79.08, 79.19, 79.19, 79.22, 79.3, 79.22, 79.16, 79.16, 79.19, 79.22, 79.24, 79.16, 79.11, 79.27, 79.27, 79.24, 79.24, 79.24, 79.24, 79.24, 79.22, 79.22, 79.22, 79.22, 79.22, 79.22, 79.22, 79.22, 79.22, 79.27, 79.27, 79.3, 79.24, 79.3, 79.3, 79.24, 79.16, 79.22, 79.19, 79.19, 79.19, 79.19, 79.22, 79.22, 79.22, 79.22, 79.24, 79.3, 79.22, 79.24, 79.19, 79.19, 79.16, 79.19, 79.19, 79.19, 79.22, 79.22, 79.22, 79.22, 79.22, 79.22, 79.22, 79.22, 79.22]
local_train = [41.89, 48.57, 48.46, 47.62, 52.0, 55.27, 54.95, 54.24, 56.3, 57.41, 54.54, 55.92, 56.0, 56.22, 58.35, 56.84, 57.54, 56.43, 56.89, 56.54, 56.73, 56.89, 57.76, 56.32, 56.7, 56.86, 56.68, 57.35, 57.32, 57.27, 57.32, 57.49, 57.54, 58.65, 57.7, 57.62, 57.73, 57.73, 57.7, 57.59, 58.05, 57.68, 57.86, 57.95, 57.84, 57.51, 57.78, 57.57, 57.7, 58.41, 57.95, 58.03, 57.16, 57.14, 57.92, 57.81, 58.05, 57.95, 57.19, 58.14, 58.14, 57.49, 58.03, 57.95, 57.68, 58.08, 57.89, 58.11, 58.03, 58.11, 58.05, 58.19, 57.97, 58.05, 58.16, 58.11, 57.97, 58.08, 58.14, 58.03, 58.08, 58.14, 58.22, 58.08, 58.24, 57.89, 58.08, 58.24, 58.22, 58.3, 58.19, 58.16, 58.14, 58.11, 58.24, 58.16, 58.16, 58.19, 58.08, 58.11, 58.05, 58.08, 58.19, 58.22, 58.19, 58.05, 58.32, 58.3, 58.11, 58.35, 58.19, 58.24, 58.14, 58.16, 58.22, 58.11, 58.19, 58.14, 58.0, 58.08, 58.22, 58.14, 58.05, 58.11, 58.08, 58.14, 58.11, 58.0, 57.97, 58.16, 58.08, 58.03, 58.16, 58.11, 58.11, 58.16, 58.05, 58.03, 57.89, 58.11, 58.05, 58.11, 58.0, 58.16, 58.32, 58.16, 58.27, 58.32, 58.41, 58.22, 58.27, 58.22, 58.24, 58.08, 58.3, 58.16, 58.08, 58.11, 58.22, 58.22, 58.32, 58.14, 58.11, 58.41, 58.35, 58.38, 58.35, 58.16, 58.22, 58.32, 58.24, 58.41, 58.3, 58.46, 58.27, 58.24, 58.59, 58.35, 58.43, 58.51, 58.46, 58.51, 58.54, 58.46, 58.38, 58.43, 58.22, 58.43, 58.38, 58.27, 58.59, 58.3, 58.35, 58.19, 58.14, 58.16, 58.16, 58.19, 58.11, 58.14]
fed_sign = [44.49, 59.03, 61.81, 62.11, 62.84, 64.68, 67.73, 68.97, 70.68, 69.92, 71.57, 70.86, 71.11, 70.95, 71.35, 71.11, 71.27, 70.86, 71.46, 73.49, 73.84, 74.08, 74.41, 74.03, 74.59, 74.97, 75.0, 75.27, 74.76, 74.97, 74.89, 75.95, 75.27, 75.51, 74.65, 75.24, 74.95, 75.49, 75.0, 75.14, 74.41, 75.51, 75.0, 74.7, 75.41, 75.49, 74.78, 75.11, 75.38, 75.78, 74.73, 75.57, 75.19, 75.59, 75.54, 75.41, 75.27, 75.41, 75.11, 74.95, 76.0, 75.7, 74.76, 74.24, 75.22, 74.49, 75.92, 74.32, 75.97, 75.54, 76.73, 75.76, 76.35, 75.84, 76.65, 75.62, 76.68, 75.78, 75.89, 75.46, 77.54, 75.03, 77.32, 76.11, 76.46, 76.05, 77.68, 75.62, 77.43, 76.22, 77.35, 75.65, 77.54, 75.68, 76.95, 76.43, 77.73, 76.65, 75.95, 76.89, 78.0, 78.89, 79.27, 79.16, 79.22, 79.24, 79.35, 79.27, 79.03, 79.19, 79.27, 79.3, 79.35, 79.22, 79.16, 79.14, 79.22, 79.38, 79.08, 79.22, 79.19, 79.27, 79.32, 79.32, 79.3, 79.22, 79.35, 79.51, 79.41, 79.41, 79.32, 79.27, 79.32, 79.41, 79.35, 79.19, 79.16, 79.3, 79.32, 79.22, 79.41, 79.3, 79.46, 79.38, 79.35, 79.38, 79.35, 79.38, 79.46, 79.46, 79.41, 79.38, 79.41, 79.41, 79.35, 79.41, 79.38, 79.38, 79.43, 79.43, 79.41, 79.38, 79.38, 79.38, 79.38, 79.41, 79.41, 79.41, 79.43, 79.35, 79.35, 79.35, 79.35, 79.32, 79.38, 79.32, 79.32, 79.35, 79.35, 79.38, 79.38, 79.35, 79.38, 79.41, 79.41, 79.41, 79.41, 79.41, 79.35, 79.35, 79.35, 79.41, 79.38, 79.38, 79.41, 79.43, 79.41, 79.41, 79.41, 79.38]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_efsign, fed_sign, fed_avg, local_train, save_path, plot_size="3")
