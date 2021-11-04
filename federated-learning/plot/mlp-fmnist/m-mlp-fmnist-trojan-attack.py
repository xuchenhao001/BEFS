import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [50.95, 53.7, 59.84, 60.92, 61.7, 62.03, 63.08, 65.65, 67.05, 67.92, 68.84, 69.16, 69.89, 70.16, 70.46, 70.68, 70.97, 71.32, 71.38, 71.43, 71.57, 71.84, 72.0, 72.08, 72.16, 72.3, 72.32, 72.41, 72.59, 72.65, 72.76, 72.86, 72.89, 73.0, 73.0, 73.08, 73.03, 73.19, 73.14, 73.14, 73.41, 73.3, 73.41, 73.38, 73.41, 73.54, 73.62, 73.51, 73.54, 73.62, 73.73, 73.59, 73.76, 73.84, 73.84, 73.92, 73.89, 73.84, 73.89, 73.86, 73.86, 73.89, 73.95, 73.97, 73.97, 73.92, 73.95, 73.97, 74.03, 74.0, 73.97, 74.0, 73.97, 73.97, 74.03, 74.03, 73.89, 73.97, 74.08, 74.05, 74.05, 74.14, 74.11, 74.08, 74.0, 74.05, 74.16, 74.05, 74.11, 74.14, 74.11, 74.05, 74.14, 74.19, 74.11, 74.19, 74.19, 74.11, 74.03, 74.14, 74.16, 74.11, 74.16, 74.19, 74.14, 74.22, 74.19, 74.19, 74.24, 74.22, 74.27, 74.19, 74.27, 74.16, 74.14, 74.16, 74.3, 74.11, 74.24, 74.14, 74.19, 74.14, 74.27, 74.35, 74.22, 74.35, 74.14, 74.3, 74.27, 74.24, 74.32, 74.19, 74.32, 74.3, 74.38, 74.22, 74.16, 74.32, 74.22, 74.16, 74.27, 74.35, 74.16, 74.35, 74.3, 74.41, 74.27, 74.38, 74.32, 74.32, 74.38, 74.38, 74.43, 74.32, 74.38, 74.35, 74.49, 74.41, 74.46, 74.38, 74.27, 74.38, 74.32, 74.27, 74.43, 74.32, 74.24, 74.38, 74.41, 74.32, 74.43, 74.41, 74.46, 74.41, 74.49, 74.38, 74.41, 74.43, 74.49, 74.41, 74.35, 74.35, 74.38, 74.41, 74.41, 74.51, 74.46, 74.41, 74.41, 74.41, 74.41, 74.54, 74.38, 74.49, 74.3, 74.49, 74.49, 74.49, 74.3, 74.43]
fed_efsign = [50.03, 58.51, 62.84, 61.76, 62.05, 61.78, 61.97, 62.19, 63.92, 65.3, 66.89, 68.27, 70.59, 71.11, 73.32, 73.62, 75.62, 75.49, 76.97, 76.76, 77.73, 77.41, 78.19, 78.11, 78.51, 78.54, 78.7, 78.76, 78.65, 78.95, 78.76, 79.08, 78.95, 78.76, 78.86, 78.76, 78.78, 78.51, 78.81, 78.27, 78.35, 78.16, 78.38, 77.97, 78.19, 77.59, 77.7, 77.86, 77.68, 77.73, 77.73, 78.03, 78.05, 78.0, 78.24, 77.89, 78.19, 77.51, 77.81, 77.46, 77.97, 77.51, 77.24, 77.54, 77.35, 77.43, 78.16, 77.16, 78.19, 77.0, 78.05, 77.03, 77.76, 76.95, 78.16, 78.14, 77.46, 76.7, 78.27, 76.84, 78.0, 76.86, 77.59, 77.84, 78.03, 78.14, 77.89, 77.95, 78.41, 78.22, 80.68, 80.11, 79.7, 80.16, 80.11, 79.89, 79.92, 79.95, 79.46, 80.03, 78.24, 79.54, 78.89, 79.49, 77.76, 79.14, 77.54, 79.3, 76.3, 79.38, 77.54, 79.11, 77.32, 78.86, 77.38, 79.41, 77.24, 79.08, 74.78, 79.35, 78.19, 79.19, 76.97, 79.3, 77.46, 79.78, 78.38, 79.86, 78.14, 79.62, 75.59, 80.08, 78.14, 79.78, 76.68, 79.7, 78.35, 79.95, 77.16, 79.89, 78.59, 79.76, 77.24, 80.22, 78.27, 79.89, 77.14, 79.76, 79.14, 79.76, 78.49, 80.03, 77.92, 79.84, 77.62, 79.86, 77.35, 80.08, 77.16, 80.14, 78.73, 79.49, 78.0, 80.16, 78.84, 79.92, 77.97, 80.05, 79.14, 80.05, 78.62, 80.0, 76.7, 79.81, 78.73, 80.05, 78.27, 79.51, 77.43, 79.68, 78.78, 79.51, 77.65, 79.86, 75.92, 79.57, 80.78, 75.08, 80.14, 75.35, 79.92, 79.43, 80.54, 80.16, 80.35, 79.76, 80.16, 80.16, 80.27, 80.24]
fed_sync = [43.16, 56.54, 60.32, 61.86, 62.49, 64.27, 66.7, 67.92, 68.97, 69.51, 69.95, 70.03, 70.35, 70.57, 70.78, 71.08, 71.43, 71.57, 71.49, 71.51, 71.62, 71.62, 71.89, 71.95, 72.08, 72.03, 72.32, 72.38, 72.46, 72.43, 72.59, 72.62, 72.51, 72.78, 72.7, 72.62, 72.84, 72.78, 73.0, 72.97, 72.92, 73.05, 72.97, 73.05, 73.05, 73.05, 73.38, 73.16, 73.38, 73.3, 73.27, 73.24, 73.3, 73.24, 73.3, 73.3, 73.32, 73.38, 73.38, 73.57, 73.57, 73.57, 73.51, 73.62, 73.43, 73.57, 73.7, 73.84, 73.76, 73.59, 73.65, 73.76, 73.7, 73.76, 73.73, 73.78, 73.86, 73.84, 73.84, 73.84, 73.76, 73.89, 73.89, 73.84, 73.76, 73.81, 73.84, 73.89, 73.92, 73.89, 73.84, 73.97, 74.0, 73.97, 73.95, 73.95, 74.0, 73.95, 74.05, 74.03, 73.97, 74.03, 74.0, 74.14, 74.08, 74.03, 74.14, 74.05, 74.05, 74.03, 74.05, 74.05, 74.11, 74.08, 74.11, 74.05, 74.03, 74.08, 74.03, 74.03, 74.05, 74.08, 74.08, 74.19, 74.05, 74.05, 74.11, 74.03, 74.19, 74.08, 74.14, 74.27, 74.22, 74.16, 74.16, 74.24, 74.3, 74.3, 74.35, 74.16, 74.35, 74.3, 74.35, 74.32, 74.24, 74.19, 74.3, 74.19, 74.24, 74.27, 74.22, 74.3, 74.19, 74.41, 74.24, 74.22, 74.3, 74.46, 74.19, 74.22, 74.3, 74.3, 74.35, 74.3, 74.27, 74.32, 74.22, 74.22, 74.3, 74.32, 74.35, 74.32, 74.35, 74.19, 74.35, 74.22, 74.24, 74.38, 74.84, 75.62, 76.43, 76.81, 76.89, 77.11, 77.08, 77.16, 77.16, 77.19, 77.32, 77.41, 77.43, 77.24, 77.35, 77.46, 77.43, 77.57, 77.43, 77.46, 77.49, 77.68]
fed_sync_sgd = [40.22, 54.84, 51.38, 56.11, 55.38, 58.41, 57.7, 61.78, 60.89, 64.38, 63.81, 66.84, 66.27, 69.27, 68.81, 71.43, 71.03, 72.97, 72.0, 74.11, 72.89, 74.73, 73.43, 75.19, 74.24, 75.54, 74.68, 76.16, 74.81, 76.41, 75.22, 76.59, 75.32, 76.7, 75.51, 76.84, 75.62, 76.95, 75.89, 77.05, 76.19, 77.14, 76.14, 77.3, 76.41, 77.3, 76.54, 77.24, 76.78, 77.35, 76.84, 77.68, 76.89, 77.73, 76.92, 77.7, 76.95, 77.78, 77.24, 77.84, 77.27, 77.89, 77.16, 77.89, 77.11, 77.84, 77.24, 77.86, 77.46, 77.92, 77.38, 78.08, 77.57, 78.14, 77.54, 78.14, 77.57, 77.97, 77.76, 78.05, 77.81, 78.19, 77.92, 78.22, 77.84, 78.19, 77.76, 78.24, 77.78, 78.38, 77.81, 78.22, 77.92, 78.22, 77.81, 78.24, 77.92, 78.27, 77.89, 78.03, 78.22, 78.3, 78.22, 78.19, 78.27, 78.35, 78.54, 78.51, 78.46, 78.43, 78.43, 78.41, 78.43, 78.57, 78.65, 78.57, 78.65, 78.84, 78.84, 78.76, 78.78, 78.86, 78.86, 78.84, 78.95, 78.97, 78.89, 78.95, 79.0, 79.03, 79.08, 79.03, 79.05, 79.05, 79.03, 79.0, 79.05, 79.11, 79.24, 79.27, 79.35, 79.3, 79.41, 79.43, 79.41, 79.41, 79.43, 79.43, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.38, 79.38, 79.38, 79.38, 79.38, 79.38, 79.41, 79.43, 79.43, 79.41, 79.41, 79.41, 79.43, 79.43, 79.43, 79.43, 79.43, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.41, 79.43, 79.43, 79.43, 79.43, 79.43, 79.43, 79.43, 79.43, 79.43]
local_train = [49.43, 61.49, 64.16, 64.43, 65.89, 68.08, 69.68, 71.35, 72.19, 73.27, 74.27, 74.27, 74.76, 74.84, 74.73, 74.89, 75.51, 75.49, 75.7, 75.68, 76.22, 76.51, 76.43, 76.3, 76.54, 76.78, 76.76, 76.84, 76.7, 77.14, 76.97, 77.19, 77.05, 76.78, 77.27, 76.97, 77.24, 77.32, 77.32, 77.22, 77.38, 77.14, 77.35, 77.38, 77.19, 77.43, 77.41, 77.41, 77.62, 77.32, 77.57, 77.22, 77.43, 77.35, 77.43, 77.49, 77.46, 77.41, 77.3, 77.62, 77.41, 77.59, 77.59, 77.41, 77.22, 77.57, 77.46, 77.49, 77.54, 77.35, 77.41, 77.46, 77.43, 77.24, 77.11, 77.68, 77.59, 77.57, 77.32, 77.51, 77.32, 77.41, 77.3, 77.35, 77.38, 77.22, 77.27, 77.27, 77.08, 77.27, 77.22, 77.3, 77.27, 77.27, 77.27, 77.24, 77.32, 77.32, 77.54, 77.24, 77.46, 77.73, 77.59, 77.65, 77.41, 77.32, 77.73, 77.49, 77.59, 77.73, 77.43, 77.95, 77.76, 78.03, 77.76, 77.65, 77.65, 77.59, 77.76, 77.65, 77.76, 77.78, 78.0, 77.81, 77.76, 78.0, 77.73, 77.86, 78.0, 77.86, 77.84, 77.86, 77.78, 77.65, 77.95, 78.0, 77.89, 77.73, 77.73, 77.68, 77.78, 77.95, 77.81, 77.51, 77.95, 77.89, 77.78, 78.0, 77.84, 77.84, 77.92, 77.57, 77.92, 77.84, 77.62, 77.84, 77.86, 77.7, 77.81, 77.49, 78.11, 77.73, 77.86, 77.95, 77.84, 77.76, 77.86, 78.03, 77.97, 77.92, 77.68, 77.78, 77.76, 77.81, 77.76, 77.73, 77.76, 77.92, 77.7, 77.81, 77.7, 77.62, 77.89, 78.0, 77.62, 77.95, 77.97, 77.89, 77.7, 78.0, 77.97, 77.76, 77.84, 77.86, 77.76, 77.78, 78.05, 77.84, 77.92, 77.95]
fed_sign_sgd = [52.7, 63.46, 66.22, 66.3, 66.89, 67.49, 70.16, 72.43, 74.19, 75.27, 75.46, 76.86, 76.32, 77.46, 76.11, 77.59, 76.73, 77.84, 77.43, 78.35, 77.41, 78.73, 78.3, 79.0, 78.59, 79.43, 79.76, 79.86, 80.62, 79.81, 80.68, 80.49, 80.57, 81.11, 82.35, 80.32, 80.68, 79.84, 80.14, 79.78, 80.81, 80.97, 81.54, 80.27, 81.46, 80.32, 81.19, 80.46, 81.95, 81.35, 82.41, 81.65, 82.76, 82.05, 83.05, 82.24, 83.05, 82.65, 82.73, 82.81, 83.16, 83.24, 82.89, 83.27, 82.14, 81.81, 82.49, 83.68, 82.86, 82.24, 81.43, 82.38, 81.97, 82.92, 81.62, 83.22, 81.57, 83.43, 82.89, 83.27, 82.38, 83.19, 83.11, 83.38, 83.11, 83.76, 83.0, 82.97, 83.65, 83.03, 82.03, 82.65, 82.19, 81.92, 83.19, 82.84, 82.46, 82.7, 82.46, 83.32, 84.11, 84.68, 84.97, 85.24, 85.41, 85.32, 85.3, 85.43, 85.3, 85.27, 85.24, 85.3, 85.41, 85.43, 85.32, 85.41, 85.35, 85.38, 85.38, 85.54, 85.51, 85.35, 85.65, 85.41, 85.54, 85.49, 85.49, 85.51, 85.51, 85.51, 85.46, 85.41, 85.59, 85.49, 85.51, 85.62, 85.65, 85.59, 85.43, 85.51, 85.54, 85.38, 85.27, 85.32, 85.51, 85.57, 85.46, 85.32, 85.46, 85.43, 85.43, 85.43, 85.46, 85.41, 85.41, 85.41, 85.41, 85.41, 85.38, 85.41, 85.49, 85.51, 85.62, 85.62, 85.59, 85.54, 85.57, 85.57, 85.59, 85.59, 85.46, 85.46, 85.49, 85.49, 85.43, 85.43, 85.41, 85.38, 85.49, 85.54, 85.54, 85.57, 85.54, 85.54, 85.46, 85.54, 85.51, 85.49, 85.49, 85.46, 85.46, 85.43, 85.41, 85.43, 85.49, 85.43, 85.51, 85.46, 85.49, 85.43]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_efsign, fed_sign_sgd, fed_avg, local_train, save_path, plot_size="3")
