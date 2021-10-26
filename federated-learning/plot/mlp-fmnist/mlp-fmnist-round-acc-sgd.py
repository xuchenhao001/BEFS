import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [38.05, 58.51, 66.81, 67.35, 67.68, 68.41, 71.51, 73.95, 74.81, 75.35, 76.08, 76.38, 76.81, 77.08, 77.22, 77.35, 77.51, 77.62, 77.73, 77.86, 77.78, 77.92, 78.0, 78.05, 78.46, 78.24, 78.32, 78.32, 78.43, 78.46, 78.59, 78.76, 78.78, 78.89, 78.84, 78.92, 78.92, 78.97, 79.03, 79.14, 78.95, 79.11, 79.22, 79.32, 79.32, 79.3, 79.41, 79.3, 79.54, 79.46, 79.32, 79.43, 79.46, 79.54, 79.51, 79.57, 79.57, 79.7, 79.57, 79.46, 79.57, 79.65, 79.73, 79.89, 79.68, 79.62, 79.84, 79.97, 79.89, 79.92, 79.7, 79.86, 80.05, 79.97, 79.97, 79.89, 79.97, 80.14, 80.19, 79.95, 80.05, 80.16, 80.03, 80.03, 80.14, 80.19, 80.27, 80.38, 79.95, 80.19, 80.3, 80.27, 80.14, 80.3, 80.08, 80.32, 80.27, 80.22, 80.32, 80.3, 80.43, 80.43, 80.41, 80.35, 80.51, 80.38, 80.14, 80.41, 80.24, 80.54, 80.38, 80.38, 80.43, 80.3, 80.27, 80.32, 80.54, 80.57, 80.46, 80.3, 80.38, 80.19, 80.46, 80.46, 80.59, 80.43, 80.46, 80.41, 80.65, 80.3, 80.43, 80.76, 80.62, 80.59, 80.59, 80.54, 80.62, 80.73, 80.59, 80.57, 80.62, 80.7, 80.73, 80.43, 80.57, 80.59, 80.46, 80.62, 80.62, 80.65, 80.65, 80.35, 80.62, 80.57, 80.86, 80.76, 80.76, 80.65, 80.38, 80.7, 80.84, 80.76, 80.32, 80.65, 80.49, 80.86, 80.78, 80.86, 80.68, 80.51, 81.05, 80.57, 80.65, 80.89, 80.84, 80.68, 80.92, 80.84, 80.95, 81.05, 80.65, 80.78, 81.05, 80.78, 80.92, 80.81, 80.92, 80.86, 80.86, 81.27, 81.14, 80.81, 80.78, 80.81, 80.73, 81.03, 80.84, 81.22, 81.16, 80.92]
fed_sync = [54.54, 62.32, 62.46, 62.89, 63.05, 63.22, 63.95, 66.89, 68.84, 70.0, 70.89, 71.14, 71.24, 71.3, 71.54, 71.81, 72.0, 72.19, 72.05, 72.54, 72.68, 72.68, 72.81, 72.97, 72.92, 73.0, 73.0, 73.05, 73.16, 73.27, 73.32, 73.38, 73.38, 73.59, 73.54, 73.57, 73.7, 73.62, 73.62, 73.65, 73.65, 73.81, 73.62, 73.84, 73.78, 73.76, 73.84, 73.7, 73.81, 73.78, 73.78, 73.92, 73.78, 73.76, 73.84, 74.0, 73.84, 74.05, 73.97, 73.97, 73.97, 73.95, 74.0, 74.22, 74.03, 73.97, 74.16, 74.19, 74.05, 74.05, 74.14, 74.16, 74.22, 74.16, 74.16, 74.19, 74.27, 74.3, 74.3, 74.27, 74.38, 74.24, 74.3, 74.22, 74.38, 74.43, 74.32, 74.41, 74.51, 74.38, 74.49, 74.49, 74.51, 74.49, 74.54, 74.38, 74.46, 74.54, 74.3, 74.41, 74.41, 74.46, 74.51, 74.54, 74.51, 74.54, 74.57, 74.51, 74.46, 74.57, 74.51, 74.57, 74.57, 74.65, 74.68, 74.54, 74.51, 74.57, 74.59, 74.73, 74.51, 74.54, 74.62, 74.49, 74.65, 74.54, 74.59, 74.43, 74.65, 74.65, 74.59, 74.54, 74.68, 74.65, 74.62, 74.62, 74.62, 74.54, 74.57, 74.76, 74.68, 74.65, 74.65, 74.76, 74.73, 74.62, 74.7, 74.68, 74.73, 74.76, 74.73, 74.65, 74.76, 74.73, 74.76, 74.7, 74.81, 74.73, 74.7, 74.68, 74.84, 74.84, 74.78, 74.78, 74.68, 74.81, 74.73, 74.86, 74.73, 74.81, 74.68, 74.76, 74.86, 74.76, 74.7, 74.81, 74.81, 74.95, 74.84, 74.76, 74.78, 74.84, 74.81, 74.84, 74.86, 74.78, 74.86, 74.78, 74.95, 74.7, 74.97, 74.95, 74.95, 75.03, 74.84, 74.89, 74.97, 74.81, 74.76, 74.92]
fed_sync_sgd = [44.81, 51.32, 54.95, 58.41, 62.89, 64.84, 64.86, 65.89, 65.32, 66.3, 66.16, 67.11, 67.65, 69.22, 69.73, 70.89, 70.89, 71.86, 71.89, 72.7, 72.81, 73.19, 73.05, 73.54, 73.54, 74.03, 73.97, 74.35, 74.35, 74.65, 74.68, 74.95, 75.05, 75.19, 75.08, 75.24, 75.32, 75.51, 75.38, 75.78, 75.68, 75.89, 75.7, 76.14, 75.81, 76.19, 76.03, 76.3, 76.22, 76.38, 76.24, 76.7, 76.24, 76.78, 76.32, 76.81, 76.3, 76.95, 76.49, 76.92, 76.68, 76.95, 76.62, 77.0, 76.7, 76.97, 76.81, 77.05, 76.86, 77.16, 76.95, 77.19, 77.05, 77.35, 77.11, 77.41, 77.19, 77.41, 77.22, 77.46, 77.27, 77.46, 77.19, 77.41, 77.19, 77.46, 77.14, 77.49, 77.27, 77.46, 77.3, 77.49, 77.27, 77.46, 77.35, 77.51, 77.38, 77.51, 77.27, 77.54, 77.3, 77.54, 77.35, 77.57, 77.43, 77.51, 77.49, 77.54, 77.57, 77.51, 77.65, 77.46, 77.57, 77.51, 77.57, 77.46, 77.54, 77.51, 77.78, 77.68, 77.76, 77.7, 77.73, 77.68, 77.68, 77.65, 77.73, 77.76, 77.73, 77.86, 77.78, 77.81, 77.81, 77.84, 77.81, 77.73, 77.81, 77.84, 77.62, 77.81, 77.73, 77.81, 77.92, 77.95, 77.84, 77.89, 77.73, 77.73, 77.95, 77.86, 77.86, 77.84, 77.81, 78.05, 77.84, 78.03, 77.92, 78.03, 77.86, 78.0, 77.84, 77.95, 77.95, 78.05, 78.11, 77.84, 78.14, 78.0, 78.16, 78.03, 78.08, 78.11, 78.16, 78.11, 78.16, 78.24, 78.03, 78.32, 78.0, 78.22, 78.11, 78.22, 78.16, 78.22, 78.16, 78.41, 78.03, 78.27, 78.03, 78.46, 78.0, 78.41, 78.05, 78.49, 78.11, 78.38, 78.05, 78.41, 78.03, 78.46]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_avg, save_path, plot_size="L")
