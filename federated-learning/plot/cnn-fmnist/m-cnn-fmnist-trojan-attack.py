import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [83.59, 86.62, 87.46, 87.92, 87.81, 88.3, 88.38, 88.59, 88.68, 88.68, 88.7, 88.59, 88.54, 88.78, 88.7, 88.68, 88.22, 88.51, 88.73, 88.38, 88.46, 88.54, 88.7, 88.51, 88.51, 88.3, 88.65, 88.57, 88.49, 88.51, 88.51, 88.57, 88.51, 88.46, 88.62, 88.65, 88.41, 88.46, 88.46, 88.41, 88.27, 88.11, 88.19, 88.27, 88.16, 88.32, 88.27, 88.19, 88.27, 88.54, 88.11, 88.14, 88.08, 88.22, 88.16, 88.24, 88.11, 87.86, 87.86, 88.08, 88.03, 88.11, 88.22, 88.19, 88.43, 88.35, 88.27, 88.43, 88.3, 88.11, 88.24, 88.19, 88.3, 88.14, 88.16, 88.14, 88.08, 88.16, 87.81, 87.84, 87.84, 87.95, 88.16, 88.0, 87.92, 88.24, 88.08, 87.95, 88.03, 87.86, 87.86, 87.89, 87.86, 87.89, 88.03, 87.89, 87.89, 87.95, 87.95, 88.03, 87.89, 87.97, 88.05, 88.08, 87.95, 87.89, 87.89, 87.84, 87.84, 88.16, 87.89, 87.84, 87.97, 87.97, 88.0, 87.81, 87.84, 87.73, 87.73, 87.84, 87.81, 87.81, 87.76, 87.76, 87.92, 87.86, 87.76, 87.84, 87.89, 87.84, 87.89, 87.84, 87.86, 87.84, 87.89, 87.86, 87.86, 87.95, 88.11, 88.3, 88.22, 88.19, 88.08, 88.16, 88.05, 88.14, 88.14, 88.05, 88.19, 88.03, 88.0, 88.11, 88.11, 88.11, 88.19, 88.16, 88.14, 88.0, 88.19, 87.97, 87.92, 87.95, 88.03, 87.97, 87.89, 87.95, 87.89, 87.84, 87.86, 87.95, 87.89, 87.97, 87.86, 87.92, 87.89, 87.89, 87.89, 87.92, 87.95, 87.84, 87.86, 87.78, 87.92, 88.03, 87.97, 88.0, 87.97, 87.97, 87.92, 87.97, 87.86, 87.89, 87.89, 88.08, 88.11, 88.05, 88.03, 88.05, 88.03, 87.97]
fed_efsign = [38.68, 50.95, 42.51, 52.84, 36.92, 48.57, 64.22, 33.51, 70.95, 39.05, 66.05, 64.41, 64.68, 71.14, 71.32, 66.16, 65.35, 64.84, 61.35, 59.54, 49.03, 44.7, 45.27, 31.68, 45.35, 26.35, 50.62, 53.27, 68.68, 66.89, 73.92, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 31.62, 41.3, 33.08, 45.76, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 75.22, 10.0, 10.0, 10.0, 10.0, 76.95, 10.0, 10.0, 10.0, 77.41, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 41.38, 69.62, 10.0, 71.38, 59.81, 50.54, 10.0, 55.65, 10.0, 50.73, 10.0, 10.0, 10.0, 71.03, 10.0, 57.89, 10.0, 67.68, 22.73, 10.0, 49.24, 10.0, 39.54, 55.81, 49.84, 63.32, 64.38, 47.11, 68.59, 77.16, 64.22, 65.78, 70.14, 73.11, 51.92, 71.84, 40.54, 68.32, 46.92, 61.38, 33.73, 58.76, 10.0, 53.03, 52.0, 54.57, 63.16]
fed_sync = [83.59, 86.35, 86.76, 87.84, 88.24, 87.97, 88.35, 88.24, 88.41, 88.51, 88.43, 88.76, 88.57, 88.43, 88.76, 88.7, 88.62, 88.81, 88.7, 88.92, 88.86, 88.59, 88.84, 88.51, 88.65, 88.65, 88.57, 88.78, 88.76, 88.54, 88.57, 88.49, 88.49, 88.41, 88.27, 88.65, 88.62, 88.3, 88.65, 88.49, 88.49, 88.54, 88.57, 88.7, 88.35, 88.3, 88.78, 88.76, 88.54, 88.46, 88.76, 88.65, 88.51, 88.57, 88.32, 88.68, 88.65, 88.46, 88.51, 88.3, 88.46, 88.35, 88.46, 88.32, 88.35, 88.24, 87.89, 88.22, 88.49, 88.3, 88.32, 88.35, 88.3, 88.32, 88.19, 87.97, 88.43, 88.08, 88.16, 88.16, 87.97, 88.05, 88.03, 88.05, 88.08, 88.08, 88.11, 88.0, 88.27, 88.3, 88.35, 88.51, 88.38, 88.14, 88.14, 88.19, 88.05, 88.03, 88.08, 88.0, 88.03, 88.0, 88.08, 88.05, 87.92, 88.03, 88.08, 88.08, 88.08, 87.92, 88.05, 87.97, 87.95, 87.95, 87.92, 87.95, 88.0, 87.95, 87.95, 87.95, 87.97, 87.89, 87.84, 87.92, 87.95, 87.92, 87.89, 87.97, 88.0, 87.97, 88.03, 87.95, 87.89, 87.86, 87.86, 87.92, 87.95, 87.97, 87.95, 88.05, 87.97, 87.97, 87.89, 88.0, 88.0, 87.92, 88.03, 88.08, 88.16, 88.14, 87.97, 88.0, 88.11, 88.05, 87.97, 88.19, 88.16, 88.11, 88.08, 88.08, 88.14, 88.05, 88.08, 88.08, 87.97, 88.16, 88.08, 88.11, 88.14, 88.05, 87.97, 88.11, 88.19, 88.43, 88.3, 88.24, 88.35, 88.11, 88.14, 88.16, 88.11, 88.22, 88.22, 88.14, 88.19, 88.14, 88.11, 88.16, 88.16, 88.03, 88.14, 88.14, 88.19, 88.08, 88.11, 88.14, 88.14, 88.22, 88.27, 88.22]
fed_sync_sgd = [25.24, 10.0, 12.86, 10.0, 4.54, 10.0, 34.97, 10.19, 47.43, 18.27, 51.68, 37.57, 53.51, 51.81, 57.05, 59.54, 60.84, 66.41, 63.86, 68.05, 65.16, 71.14, 65.19, 71.62, 65.03, 71.86, 65.97, 71.68, 66.51, 72.76, 67.43, 72.76, 68.78, 73.0, 68.38, 72.73, 69.41, 72.73, 70.22, 73.81, 71.43, 73.76, 72.11, 74.7, 73.22, 76.19, 74.3, 77.16, 75.11, 78.27, 75.95, 78.81, 76.97, 79.14, 77.03, 79.22, 77.27, 80.35, 78.62, 81.11, 78.73, 81.41, 79.41, 81.89, 79.65, 82.41, 80.08, 83.16, 81.24, 83.57, 82.05, 84.46, 82.57, 84.59, 83.3, 84.7, 84.05, 85.11, 84.51, 85.57, 85.14, 85.89, 85.76, 86.49, 85.89, 86.49, 86.51, 86.65, 86.73, 87.08, 87.38, 87.22, 87.51, 87.03, 87.57, 87.46, 87.81, 87.7, 88.08, 88.0, 88.22, 88.3, 88.46, 88.51, 88.57, 88.49, 88.51, 88.65, 88.62, 88.73, 88.62, 88.76, 88.68, 88.57, 88.62, 88.62, 88.68, 88.65, 88.68, 88.54, 88.68, 88.65, 88.68, 88.68, 88.78, 88.81, 88.73, 88.7, 88.73, 88.59, 88.54, 88.54, 88.54, 88.54, 88.59, 88.49, 88.62, 88.57, 88.59, 88.59, 88.59, 88.65, 88.7, 88.65, 88.7, 88.7, 88.68, 88.65, 88.68, 88.68, 88.68, 88.68, 88.68, 88.65, 88.65, 88.68, 88.65, 88.65, 88.65, 88.54, 88.54, 88.54, 88.54, 88.57, 88.65, 88.65, 88.65, 88.62, 88.65, 88.65, 88.68, 88.68, 88.68, 88.68, 88.7, 88.68, 88.68, 88.65, 88.62, 88.59, 88.59, 88.62, 88.62, 88.65, 88.59, 88.59, 88.59, 88.59, 88.59, 88.57, 88.51, 88.51, 88.51, 88.51, 88.51, 88.49, 88.49, 88.51, 88.51, 88.54]
local_train = [81.32, 82.35, 82.43, 84.11, 85.24, 85.22, 85.11, 85.24, 85.27, 85.27, 85.3, 85.24, 85.27, 85.16, 85.14, 85.41, 85.3, 85.3, 85.27, 85.35, 85.19, 85.32, 85.35, 85.32, 85.27, 85.35, 85.46, 85.27, 85.3, 85.27, 85.46, 85.27, 85.16, 85.35, 85.22, 85.14, 85.38, 85.41, 85.35, 85.19, 85.14, 85.3, 85.24, 85.38, 85.32, 85.41, 85.24, 85.43, 85.19, 85.32, 85.3, 85.38, 85.24, 85.32, 85.35, 85.32, 85.38, 85.3, 85.27, 85.3, 85.41, 85.27, 85.22, 85.3, 85.35, 85.32, 85.3, 85.27, 85.27, 85.43, 85.38, 85.35, 85.32, 85.3, 85.24, 85.41, 85.22, 85.3, 85.3, 85.35, 85.32, 85.32, 85.32, 85.32, 85.27, 85.3, 85.35, 85.27, 85.35, 85.43, 85.3, 85.3, 85.32, 85.35, 85.51, 85.41, 85.35, 85.3, 85.32, 85.32, 85.51, 85.46, 85.43, 85.35, 85.35, 85.54, 85.46, 85.32, 85.38, 85.35, 85.3, 85.3, 85.22, 85.41, 85.46, 85.35, 85.43, 85.32, 85.32, 85.38, 85.43, 85.35, 85.43, 85.43, 85.32, 85.41, 85.24, 85.27, 85.3, 85.41, 85.22, 85.3, 85.38, 85.35, 85.49, 85.38, 85.3, 85.38, 85.3, 85.38, 85.43, 85.32, 85.35, 85.22, 85.35, 85.3, 85.38, 85.35, 85.27, 85.32, 85.38, 85.38, 85.35, 85.32, 85.35, 85.32, 85.32, 85.24, 85.24, 85.43, 85.3, 85.38, 85.27, 85.38, 85.32, 85.3, 85.38, 85.27, 85.41, 85.3, 85.27, 85.24, 85.38, 85.35, 85.3, 85.41, 85.22, 85.27, 85.41, 85.27, 85.41, 85.41, 85.27, 85.38, 85.41, 85.43, 85.24, 85.3, 85.32, 85.43, 85.24, 85.32, 85.3, 85.43, 85.41, 85.32, 85.46, 85.35, 85.32, 85.32]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_efsign, fed_avg, local_train, save_path, plot_size="M")