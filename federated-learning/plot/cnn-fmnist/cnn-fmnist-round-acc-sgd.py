import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [83.68, 86.54, 87.05, 87.51, 88.35, 88.16, 88.62, 88.84, 89.08, 88.97, 89.05, 89.16, 89.19, 89.19, 89.16, 89.03, 89.16, 89.08, 88.97, 89.19, 89.16, 89.19, 89.05, 89.32, 89.27, 89.57, 89.03, 89.05, 89.14, 89.27, 89.24, 89.08, 89.03, 88.92, 88.89, 88.84, 89.08, 88.97, 89.03, 89.03, 89.08, 88.84, 89.03, 89.05, 88.97, 88.81, 89.14, 88.89, 88.95, 88.81, 89.03, 88.84, 89.16, 89.0, 88.97, 88.84, 89.3, 88.84, 89.14, 89.0, 89.03, 88.65, 88.73, 88.65, 88.97, 88.95, 88.89, 89.05, 88.89, 89.08, 88.62, 88.7, 88.95, 88.84, 88.95, 88.95, 88.84, 89.0, 88.73, 89.03, 88.68, 88.95, 88.62, 88.54, 88.62, 88.68, 88.62, 88.7, 88.76, 88.7, 88.81, 88.65, 88.7, 88.62, 88.51, 88.68, 88.65, 88.7, 88.92, 88.92, 88.81, 88.81, 88.86, 88.76, 88.73, 88.7, 88.84, 88.7, 88.7, 88.68, 88.73, 88.73, 88.65, 88.76, 88.65, 88.62, 88.73, 88.73, 88.68, 88.78, 88.68, 88.86, 88.92, 88.57, 88.73, 88.68, 88.92, 88.62, 89.08, 88.92, 88.84, 88.81, 88.89, 88.78, 88.89, 88.81, 88.76, 88.78, 88.73, 88.68, 88.73, 88.73, 88.84, 88.81, 88.81, 88.86, 88.84, 88.89, 88.84, 88.76, 88.73, 88.68, 88.76, 88.81, 88.86, 88.73, 88.59, 88.76, 88.73, 88.7, 88.65, 88.84, 88.73, 88.65, 88.76, 88.89, 88.81, 88.86, 88.84, 88.78, 88.81, 88.65, 88.73, 88.86, 88.89, 88.65, 88.68, 88.57, 88.68, 88.65, 88.54, 88.68, 88.7, 88.54, 88.54, 88.54, 88.62, 88.68, 88.46, 88.65, 88.68, 88.51, 88.54, 88.54, 88.59, 88.76, 88.84, 89.22, 88.97, 88.76]
fed_sync = [84.65, 86.38, 87.43, 88.16, 88.16, 88.7, 88.38, 88.92, 88.84, 89.22, 89.11, 89.03, 89.57, 89.35, 89.24, 89.0, 89.05, 89.03, 88.78, 88.97, 88.73, 88.68, 88.92, 88.76, 88.65, 88.68, 88.54, 88.7, 88.59, 88.65, 88.65, 88.68, 88.38, 88.49, 88.51, 88.38, 88.51, 88.68, 88.57, 88.86, 88.62, 88.89, 88.78, 88.41, 88.59, 88.3, 88.43, 88.51, 88.68, 88.73, 88.78, 88.65, 88.49, 88.59, 88.54, 88.68, 88.59, 88.54, 88.51, 88.49, 88.51, 88.59, 88.65, 88.35, 88.3, 88.19, 88.38, 88.38, 88.46, 88.51, 88.27, 88.38, 88.43, 88.59, 88.7, 88.57, 88.62, 88.59, 88.46, 88.49, 88.49, 88.59, 88.41, 88.54, 88.65, 88.3, 88.54, 88.51, 88.41, 88.38, 88.43, 88.43, 88.14, 88.32, 88.46, 88.03, 88.3, 88.27, 88.19, 88.27, 88.24, 88.32, 88.32, 88.16, 88.43, 88.27, 88.3, 88.38, 88.41, 88.46, 88.41, 88.38, 88.35, 88.43, 88.49, 88.46, 88.35, 88.43, 88.41, 88.27, 88.41, 88.32, 88.3, 88.3, 88.24, 88.32, 88.32, 88.3, 88.35, 88.3, 88.32, 88.27, 88.3, 88.35, 88.43, 88.3, 88.24, 88.27, 88.24, 88.32, 88.3, 88.27, 88.32, 88.27, 88.27, 88.32, 88.41, 88.38, 88.35, 88.3, 88.38, 88.32, 88.38, 88.35, 88.43, 88.59, 88.65, 88.51, 88.51, 88.51, 88.49, 88.49, 88.43, 88.46, 88.43, 88.35, 88.51, 88.46, 88.32, 88.32, 88.38, 88.35, 88.41, 88.41, 88.41, 88.46, 88.46, 88.49, 88.38, 88.46, 88.57, 88.46, 88.46, 88.41, 88.35, 88.35, 88.43, 88.24, 88.27, 88.35, 88.35, 88.38, 88.35, 88.24, 88.32, 88.3, 88.3, 88.3, 88.27, 88.3]
fed_sync_sgd = [28.11, 0.05, 23.51, 9.95, 24.49, 10.0, 25.08, 13.11, 46.41, 31.24, 56.11, 42.03, 60.08, 50.32, 61.19, 58.38, 63.89, 63.59, 67.78, 67.3, 69.97, 69.14, 71.57, 70.16, 72.86, 70.92, 74.08, 71.35, 74.78, 72.05, 74.65, 72.59, 74.73, 73.11, 75.24, 73.05, 75.81, 73.7, 76.05, 73.92, 76.49, 74.05, 77.24, 75.08, 77.92, 75.81, 78.16, 76.27, 78.59, 77.22, 79.41, 77.51, 79.51, 78.16, 79.97, 78.43, 80.41, 78.7, 80.81, 79.27, 80.97, 80.11, 81.35, 80.35, 81.3, 80.92, 81.65, 81.3, 81.62, 81.89, 82.0, 82.22, 82.65, 83.19, 83.3, 83.76, 83.3, 84.05, 83.51, 83.92, 83.65, 84.16, 84.59, 85.05, 85.03, 85.65, 85.62, 86.05, 86.43, 86.78, 87.16, 86.84, 87.38, 87.0, 87.7, 87.49, 88.22, 88.22, 88.41, 58.32, 10.0, 88.0, 88.41, 88.03, 88.0, 88.14, 88.03, 88.03, 88.14, 88.08, 88.46, 88.14, 88.16, 88.0, 88.22, 87.89, 88.11, 88.11, 88.27, 88.16, 88.14, 88.03, 87.89, 87.97, 88.14, 88.05, 88.32, 88.22, 87.95, 88.19, 87.86, 87.97, 88.38, 88.22, 88.22, 88.11, 88.11, 87.95, 88.14, 88.08, 88.05, 87.86, 87.97, 87.76, 88.49, 87.97, 88.38, 87.81, 88.35, 87.89, 88.22, 87.95, 87.97, 87.95, 88.3, 88.08, 88.3, 87.76, 88.22, 88.08, 88.3, 88.11, 88.24, 88.11, 88.19, 88.3, 88.22, 88.03, 88.22, 87.89, 88.08, 87.81, 88.22, 87.57, 88.03, 87.84, 88.24, 87.76, 87.92, 87.78, 88.0, 87.84, 88.08, 87.73, 88.32, 87.78, 88.22, 87.89, 87.84, 87.76, 88.35, 88.08, 88.24, 88.0, 87.92, 87.97, 88.22, 88.05, 88.24, 88.22]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_avg, save_path, plot_size="L")
