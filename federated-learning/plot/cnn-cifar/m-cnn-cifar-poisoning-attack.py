import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [22.11, 34.38, 40.92, 44.41, 45.59, 47.89, 48.68, 49.22, 51.16, 51.41, 51.68, 52.78, 53.51, 53.68, 53.51, 54.35, 54.08, 54.14, 53.51, 55.0, 54.11, 54.68, 55.38, 55.35, 55.11, 54.7, 55.68, 55.76, 55.84, 55.08, 55.16, 55.11, 55.32, 55.59, 55.54, 56.05, 55.76, 55.35, 55.78, 55.57, 55.49, 55.65, 55.35, 55.41, 55.76, 55.46, 56.05, 55.35, 55.57, 56.14, 55.59, 55.76, 55.43, 55.46, 55.32, 54.89, 54.7, 55.32, 55.05, 55.22, 55.22, 55.11, 55.32, 55.38, 55.81, 55.08, 55.27, 55.35, 55.08, 55.54, 55.68, 54.86, 55.16, 55.19, 55.27, 55.08, 55.05, 55.35, 55.11, 55.22, 55.14, 56.0, 55.16, 55.49, 55.76, 55.54, 55.43, 55.7, 54.78, 55.43, 55.65, 54.89, 55.84, 55.32, 55.89, 56.19, 56.24, 55.3, 55.97, 56.03, 55.92, 56.35, 56.43, 55.89, 55.68, 55.76, 55.97, 56.05, 56.22, 56.11, 56.03, 56.38, 56.54, 56.3, 56.22, 55.97, 56.0, 55.81, 56.19, 56.51, 56.27, 55.35, 56.03, 56.03, 56.24, 56.08, 55.27, 55.73, 55.46, 55.32, 55.86, 55.95, 55.41, 55.24, 55.16, 55.76, 55.84, 55.59, 55.65, 55.68, 55.38, 55.41, 55.49, 55.89, 55.57, 55.35, 55.16, 54.84, 55.46, 55.16, 55.92, 55.86, 55.27, 55.49, 55.38, 54.97, 55.27, 55.3, 55.11, 55.38, 55.57, 55.38, 55.49, 55.62, 55.54, 55.41, 54.68, 55.46, 55.84, 55.0, 54.84, 55.3, 54.43, 56.35, 55.73, 54.92, 54.92, 55.35, 55.22, 55.54, 55.49, 55.41, 55.16, 54.78, 55.22, 55.24, 54.92, 55.35, 55.51, 55.0, 55.32, 55.38, 55.35, 55.0, 55.24, 55.14, 55.41, 55.19, 55.81, 54.95]
fed_efsign = [13.65, 19.05, 9.51, 10.54, 9.32, 10.0, 10.81, 9.95, 14.16, 10.0, 10.03, 13.22, 10.05, 8.19, 5.51, 10.03, 9.81, 10.22, 10.49, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
fed_sync = [22.05, 30.3, 37.57, 42.89, 46.27, 46.59, 48.16, 49.08, 50.59, 50.78, 51.51, 52.62, 52.86, 53.11, 52.62, 52.49, 53.0, 52.89, 52.89, 53.11, 52.97, 53.03, 52.14, 52.81, 53.41, 53.89, 53.05, 53.32, 52.81, 53.57, 54.03, 53.57, 54.03, 54.46, 54.19, 53.95, 54.57, 54.3, 54.51, 54.59, 53.84, 53.78, 54.89, 53.81, 54.3, 54.22, 54.65, 54.3, 54.3, 55.05, 54.78, 54.3, 54.59, 54.27, 54.3, 54.78, 54.81, 54.81, 54.89, 55.16, 55.11, 54.92, 54.46, 54.92, 54.3, 54.86, 54.51, 54.73, 54.43, 55.19, 54.59, 54.24, 54.59, 54.62, 55.32, 55.24, 54.68, 55.05, 54.81, 54.7, 54.49, 54.81, 55.7, 54.86, 54.73, 54.76, 54.97, 54.16, 54.46, 54.35, 54.62, 53.84, 55.38, 55.57, 54.76, 55.65, 54.35, 54.62, 54.35, 55.05, 54.78, 54.57, 54.16, 54.59, 54.65, 54.57, 54.76, 53.86, 54.84, 55.7, 54.3, 54.11, 55.16, 54.22, 53.95, 54.95, 54.03, 54.27, 54.68, 54.97, 55.03, 54.14, 54.38, 54.73, 54.3, 54.57, 54.49, 54.95, 54.08, 55.0, 53.89, 53.7, 54.35, 54.73, 54.68, 54.57, 54.05, 54.41, 54.59, 55.0, 54.49, 53.65, 54.59, 54.14, 53.0, 54.22, 53.89, 54.38, 54.59, 54.57, 53.92, 54.49, 54.54, 54.49, 54.03, 54.3, 55.22, 54.97, 54.08, 54.38, 53.97, 54.24, 54.59, 54.27, 54.19, 54.81, 54.32, 54.49, 54.49, 54.14, 54.59, 55.24, 54.57, 54.16, 54.54, 54.24, 54.24, 54.78, 54.27, 55.16, 54.81, 53.54, 54.35, 54.78, 54.84, 55.03, 54.68, 55.11, 54.35, 54.43, 54.43, 55.19, 54.92, 54.95, 54.35, 54.7, 54.76, 54.24, 54.24, 54.86]
fed_sync_sgd = [21.14, 19.19, 26.86, 32.62, 35.95, 39.16, 40.7, 42.68, 44.84, 45.73, 46.19, 47.92, 47.38, 48.57, 48.97, 49.73, 49.97, 51.24, 51.54, 52.0, 52.38, 52.84, 52.35, 53.08, 52.95, 53.22, 53.38, 52.57, 52.7, 52.78, 52.78, 53.05, 52.62, 52.89, 53.0, 52.68, 52.19, 52.22, 52.46, 52.19, 52.05, 52.22, 52.43, 52.27, 52.35, 52.59, 52.65, 52.62, 52.92, 53.0, 53.11, 52.92, 53.03, 52.92, 53.08, 52.81, 53.0, 52.89, 52.59, 52.78, 52.92, 52.59, 52.54, 53.08, 52.76, 52.62, 52.51, 52.81, 52.51, 52.73, 52.03, 51.95, 52.19, 52.32, 52.27, 52.41, 52.38, 51.7, 51.89, 51.68, 51.78, 51.97, 51.89, 51.89, 51.84, 51.97, 51.54, 51.35, 51.59, 51.49, 51.65, 51.41, 51.27, 51.54, 51.3, 51.27, 51.05, 50.68, 50.27, 50.32, 50.59, 50.62, 50.7, 50.78, 50.68, 50.7, 50.78, 50.84, 50.78, 50.73, 50.65, 50.81, 50.78, 50.86, 50.89, 50.95, 50.89, 50.73, 50.54, 50.78, 50.76, 50.76, 50.81, 50.7, 50.51, 50.57, 50.62, 50.59, 50.65, 50.59, 50.81, 50.76, 50.76, 50.76, 50.73, 50.81, 50.81, 50.84, 50.89, 50.84, 50.81, 50.65, 50.65, 50.73, 50.73, 50.7, 50.7, 50.65, 50.59, 50.59, 50.57, 50.62, 50.62, 50.65, 50.65, 50.62, 50.62, 50.62, 50.65, 50.65, 50.65, 50.65, 50.65, 50.59, 50.57, 50.57, 50.54, 50.57, 50.54, 50.57, 50.57, 50.59, 50.59, 50.57, 50.57, 50.59, 50.57, 50.57, 50.62, 50.62, 50.62, 50.62, 50.59, 50.59, 50.57, 50.57, 50.65, 50.65, 50.65, 50.65, 50.65, 50.65, 50.65, 50.68, 50.7, 50.7, 50.7, 50.7, 50.73, 50.73]
local_train = [20.89, 29.49, 34.19, 35.59, 35.32, 34.51, 35.49, 36.73, 36.97, 37.49, 37.41, 37.43, 37.49, 37.38, 37.32, 37.3, 37.3, 37.38, 37.3, 37.22, 37.3, 37.27, 37.19, 37.22, 37.19, 37.22, 37.3, 37.22, 37.27, 37.32, 37.3, 37.32, 37.32, 37.35, 37.35, 37.3, 37.35, 37.35, 37.3, 37.3, 37.3, 37.32, 37.32, 37.32, 37.35, 37.32, 37.32, 37.32, 37.35, 37.3, 37.3, 37.3, 37.27, 37.27, 37.27, 37.27, 37.27, 37.24, 37.27, 37.24, 37.27, 37.3, 37.32, 37.3, 37.3, 37.3, 37.27, 37.24, 37.24, 37.3, 37.24, 37.22, 37.24, 37.24, 37.27, 37.27, 37.32, 37.32, 37.32, 37.3, 37.35, 37.3, 37.27, 37.27, 37.27, 37.27, 37.3, 37.27, 37.27, 37.27, 37.27, 37.3, 37.3, 37.3, 37.3, 37.3, 37.27, 37.27, 37.24, 37.24, 37.27, 37.24, 37.27, 37.22, 37.24, 37.27, 37.3, 37.27, 37.27, 37.3, 37.27, 37.32, 37.32, 37.32, 37.32, 37.3, 37.3, 37.3, 37.27, 37.27, 37.27, 37.24, 37.24, 37.24, 37.24, 37.24, 37.24, 37.24, 37.27, 37.27, 37.24, 37.24, 37.3, 37.27, 37.27, 37.24, 37.24, 37.24, 37.24, 37.24, 37.27, 37.27, 37.27, 37.3, 37.3, 37.3, 37.3, 37.32, 37.38, 37.35, 37.38, 37.46, 37.46, 37.46, 37.49, 37.49, 37.46, 37.49, 37.46, 37.46, 37.41, 37.43, 37.43, 37.43, 37.43, 37.43, 37.43, 37.43, 37.43, 37.41, 37.46, 37.46, 37.43, 37.43, 37.43, 37.43, 37.43, 37.43, 37.43, 37.43, 37.43, 37.41, 37.41, 37.41, 37.41, 37.41, 37.41, 37.41, 37.41, 37.41, 37.41, 37.41, 37.41, 37.41, 37.43, 37.43, 37.43, 37.43, 37.43, 37.43]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_efsign, fed_avg, local_train, save_path, plot_size="M")
