import sys

from plot.utils.time_acc_base import plot_ddos_acc

fed_avg = [26.97, 35.08, 35.08, 41.14, 41.14, 41.14, 41.03, 46.65, 47.62, 43.68, 43.46, 48.03, 48.03, 44.97, 44.97, 44.97, 48.57, 48.57, 48.57, 45.7, 45.7, 45.7, 45.7, 45.7, 45.7, 45.7, 47.19, 47.51, 47.51, 47.51, 46.46, 46.46, 46.16, 46.03, 48.16, 48.16, 50.65, 50.65, 50.59, 45.78, 45.78, 45.78, 47.89, 47.78, 48.65, 46.76, 46.76, 46.76, 48.95, 48.95, 48.95, 48.95, 48.95, 48.95, 48.95, 48.95, 50.89, 50.89, 50.89, 50.89, 50.89, 50.89, 47.92, 47.92, 47.92, 47.54, 48.78, 48.78, 48.78, 48.78, 48.49, 48.97, 48.97, 48.97, 48.97, 48.97, 50.54, 50.54, 50.54, 50.54, 50.54, 50.54, 50.54, 50.54, 50.54, 48.86, 49.46, 49.46, 47.97, 47.97, 49.86, 49.86, 49.86, 47.92, 47.92, 48.0, 48.0, 48.0, 48.0, 47.19, 47.19, 47.19, 47.19, 47.19, 47.19, 49.14, 49.14, 49.14, 48.57, 48.57, 48.57, 48.57, 47.54, 47.54, 48.41, 48.41, 48.41, 48.41, 48.41, 48.41, 48.41, 48.41, 49.65, 49.65, 48.32, 48.32, 48.32, 49.22, 49.22, 49.22, 49.22, 49.22, 49.22, 49.22, 49.22, 49.22, 47.97, 47.97, 47.97, 47.97, 47.97, 47.97, 47.97, 49.51, 49.51, 50.11, 49.76, 49.76, 49.73, 49.73, 49.73, 49.73, 49.73, 49.3, 49.3, 49.3, 49.3, 49.3, 49.3, 49.3, 49.3, 47.14, 47.14, 47.14, 47.14, 47.16, 47.16, 47.16, 47.16, 48.14, 49.49, 49.35, 49.35, 49.35, 48.95, 48.32, 49.08, 49.08, 48.24, 48.24, 47.3, 47.3, 48.78, 48.08, 48.08, 49.11, 49.11, 48.54, 49.0, 46.95, 46.95, 47.19, 48.03, 48.03, 48.03, 48.03, 48.03, 48.03, 48.89, 48.78]
fed_efsign = [11.7, 22.92, 26.95, 32.43, 34.65, 37.38, 39.35, 40.46, 43.43, 44.49, 47.03, 46.08, 48.32, 47.11, 49.76, 49.05, 50.46, 49.0, 50.54, 49.65, 50.38, 49.49, 50.16, 49.7, 49.22, 50.49, 48.92, 48.57, 49.73, 49.59, 48.92, 49.27, 50.22, 48.14, 49.49, 49.86, 49.78, 48.51, 49.46, 49.05, 48.59, 48.03, 48.03, 48.46, 47.54, 47.95, 47.76, 48.49, 48.05, 48.68, 47.97, 48.19, 47.41, 47.0, 47.76, 46.38, 47.3, 47.27, 46.41, 46.89, 47.19, 48.76, 46.84, 47.7, 46.24, 47.51, 46.35, 45.97, 46.08, 46.05, 46.41, 46.43, 47.08, 46.49, 46.81, 46.38, 45.51, 46.86, 47.35, 46.59, 47.35, 47.03, 47.38, 47.11, 45.54, 47.24, 46.78, 46.38, 46.73, 46.24, 46.89, 46.89, 45.62, 47.19, 45.46, 45.95, 46.35, 45.89, 46.59, 45.89, 46.89, 46.14, 46.14, 46.7, 46.16, 44.84, 44.92, 45.95, 46.14, 44.73, 45.03, 42.11, 45.81, 44.68, 45.38, 45.68, 45.14, 43.86, 45.22, 45.22, 45.76, 44.84, 45.16, 45.3, 45.78, 44.81, 45.81, 44.03, 46.0, 45.43, 45.24, 46.05, 45.3, 43.89, 44.65, 43.43, 44.24, 44.11, 45.03, 44.54, 43.14, 43.11, 43.73, 46.41, 43.51, 45.68, 43.57, 44.03, 44.32, 43.19, 44.22, 45.05, 45.0, 45.05, 43.97, 44.65, 43.62, 44.11, 45.95, 44.78, 44.54, 43.49, 43.95, 43.57, 45.95, 42.03, 43.24, 43.46, 43.7, 42.7, 43.78, 43.51, 43.24, 42.95, 43.65, 42.95, 42.59, 41.84, 42.57, 42.03, 42.86, 42.14, 42.68, 41.03, 41.68, 42.92, 42.54, 43.49, 43.16, 40.59, 42.68, 41.46, 43.35, 41.3, 41.41, 43.22, 43.84, 43.57, 43.11, 42.97]
fed_sign = [21.78, 26.3, 36.0, 43.46, 44.03, 45.24, 46.65, 48.38, 49.95, 50.05, 50.0, 50.16, 50.49, 50.68, 51.08, 51.59, 51.76, 51.62, 51.57, 51.14, 51.27, 51.86, 51.68, 51.46, 51.32, 51.78, 51.76, 51.24, 50.27, 50.46, 50.11, 50.68, 50.49, 50.59, 50.35, 50.46, 49.92, 49.73, 49.65, 49.22, 49.22, 49.35, 49.97, 49.49, 49.86, 49.68, 48.65, 48.19, 48.68, 48.3, 48.3, 48.08, 48.27, 48.14, 47.57, 48.03, 48.11, 47.16, 47.14, 46.97, 47.35, 47.19, 47.86, 47.81, 47.86, 47.51, 47.43, 47.54, 46.89, 47.11, 47.08, 46.97, 46.65, 46.68, 46.51, 46.38, 46.57, 47.3, 46.49, 47.08, 46.54, 47.11, 46.7, 47.3, 48.03, 47.92, 47.11, 46.92, 46.89, 46.78, 46.59, 45.95, 46.16, 46.73, 46.35, 46.32, 46.3, 46.32, 46.14, 46.03, 45.89, 45.84, 46.08, 46.38, 46.35, 46.11, 46.14, 46.27, 46.11, 46.35, 46.51, 46.65, 46.62, 46.76, 46.81, 46.78, 46.68, 46.78, 46.84, 47.0, 46.97, 47.08, 47.22, 47.16, 47.41, 47.35, 47.41, 47.14, 47.3, 47.0, 47.43, 47.16, 47.14, 47.54, 47.32, 47.46, 47.46, 47.49, 47.62, 47.49, 47.49, 47.62, 47.27, 47.54, 47.43, 47.41, 47.14, 47.57, 47.32, 47.41, 47.41, 47.24, 47.11, 47.08, 47.11, 47.22, 47.24, 47.35, 47.35, 47.27, 47.19, 47.32, 47.32, 47.38, 47.41, 47.32, 47.32, 47.32, 47.35, 47.35, 47.3, 47.32, 47.46, 47.46, 47.46, 47.46, 47.49, 47.43, 47.46, 47.51, 47.51, 47.54, 47.54, 47.54, 47.57, 47.59, 47.68, 47.68, 47.68, 47.68, 47.65, 47.65, 47.65, 47.65, 47.65, 47.62, 47.57, 47.59, 47.62, 47.65]
fed_sync_sgd = [23.7, 18.16, 31.68, 32.86, 37.49, 39.54, 41.22, 44.14, 45.11, 46.03, 47.46, 48.41, 49.08, 49.32, 50.51, 50.54, 51.35, 51.16, 52.03, 52.3, 52.05, 51.68, 51.86, 51.62, 51.68, 51.35, 51.3, 50.95, 50.76, 51.11, 51.19, 51.7, 51.92, 51.65, 51.76, 51.22, 51.51, 50.97, 51.3, 51.27, 51.14, 50.76, 51.11, 50.81, 51.05, 50.86, 50.59, 50.54, 50.43, 50.08, 50.16, 50.05, 50.19, 50.0, 49.95, 49.7, 49.84, 50.27, 50.19, 50.03, 49.84, 49.92, 50.22, 49.95, 49.7, 49.81, 49.86, 50.0, 49.57, 49.68, 49.3, 49.38, 49.22, 49.38, 49.27, 49.08, 49.03, 48.41, 48.84, 48.95, 48.92, 48.92, 48.57, 48.62, 48.7, 48.46, 48.89, 48.35, 48.35, 48.16, 48.14, 48.59, 48.46, 48.43, 48.46, 48.3, 48.59, 47.89, 47.57, 47.49, 47.62, 47.65, 47.59, 47.54, 47.62, 47.54, 47.38, 47.43, 47.57, 47.57, 47.7, 47.68, 47.81, 47.78, 47.78, 47.84, 47.76, 47.89, 47.89, 47.97, 48.08, 48.08, 48.05, 48.11, 48.14, 48.16, 48.19, 48.27, 48.27, 48.22, 48.27, 48.14, 48.16, 48.22, 48.16, 48.16, 48.14, 48.11, 48.11, 48.03, 48.03, 48.11, 48.08, 48.11, 48.16, 48.14, 48.11, 48.14, 48.22, 48.22, 48.22, 48.22, 48.22, 48.22, 48.22, 48.22, 48.24, 48.27, 48.24, 48.22, 48.22, 48.27, 48.3, 48.3, 48.3, 48.3, 48.32, 48.32, 48.3, 48.27, 48.27, 48.3, 48.32, 48.32, 48.35, 48.3, 48.32, 48.32, 48.35, 48.38, 48.38, 48.38, 48.41, 48.41, 48.41, 48.41, 48.35, 48.35, 48.35, 48.41, 48.38, 48.38, 48.38, 48.41, 48.38, 48.32, 48.32, 48.32, 48.3, 48.3]

# fed_avg = [26.97, 35.08, 35.08, 41.14, 41.14, 41.14, 41.03, 46.65, 47.62, 43.68, 43.46, 48.03, 48.03, 44.97, 44.97, 44.97, 48.57, 48.57, 48.57, 45.7, 45.7, 45.7, 45.7, 45.7, 45.7, 45.7, 47.19, 47.51, 47.51, 47.51, 46.46, 46.46, 46.16, 46.03, 48.16, 48.16, 50.65, 50.65, 50.59, 45.78, 45.78, 45.78, 47.89, 47.78, 48.65, 46.76, 46.76, 46.76, 48.95, 48.95]
# fed_efsign = [11.7, 22.92, 26.95, 32.43, 34.65, 37.38, 39.35, 40.46, 43.43, 44.49, 47.03, 46.08, 48.32, 47.11, 49.76, 49.05, 50.46, 49.0, 50.54, 49.65, 50.38, 49.49, 50.16, 49.7, 49.22, 50.49, 48.92, 48.57, 49.73, 49.59, 48.92, 49.27, 50.22, 48.14, 49.49, 49.86, 49.78, 48.51, 49.46, 49.05, 48.59, 48.03, 48.03, 48.46, 47.54, 47.95, 47.76, 48.49, 48.05, 48.68]
# fed_sign = [21.78, 26.3, 36.0, 43.46, 44.03, 45.24, 46.65, 48.38, 49.95, 50.05, 50.0, 50.16, 50.49, 50.68, 51.08, 51.59, 51.76, 51.62, 51.57, 51.14, 51.27, 51.86, 51.68, 51.46, 51.32, 51.78, 51.76, 51.24, 50.27, 50.46, 50.11, 50.68, 50.49, 50.59, 50.35, 50.46, 49.92, 49.73, 49.65, 49.22, 49.22, 49.35, 49.97, 49.49, 49.86, 49.68, 48.65, 48.19, 48.68, 48.3]
# fed_sync_sgd = [23.7, 18.16, 31.68, 32.86, 37.49, 39.54, 41.22, 44.14, 45.11, 46.03, 47.46, 48.41, 49.08, 49.32, 50.51, 50.54, 51.35, 51.16, 52.03, 52.3, 52.05, 51.68, 51.86, 51.62, 51.68, 51.35, 51.3, 50.95, 50.76, 51.11, 51.19, 51.7, 51.92, 51.65, 51.76, 51.22, 51.51, 50.97, 51.3, 51.27, 51.14, 50.76, 51.11, 50.81, 51.05, 50.86, 50.59, 50.54, 50.43, 50.08]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_ddos_acc("", fed_sync_sgd, fed_avg, fed_efsign, fed_sign, save_path, plot_size="4")
