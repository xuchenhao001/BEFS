import sys

from plot.utils.time_acc_base import plot_time_acc_attack

fed_avg_ddos095 = [26.73, 26.73, 26.73, 26.73, 26.73, 26.73, 26.73, 26.73, 26.73, 33.73, 38.9, 41.7, 41.7, 41.7, 41.7, 41.7, 41.7, 41.93, 45.27, 44.9, 43.03, 42.87, 42.43, 45.63, 45.63, 45.63, 45.63, 44.4, 44.03, 44.03, 46.67, 46.67, 46.67, 45.73, 45.73, 45.73, 46.13, 46.13, 44.4, 44.4, 44.4, 46.1, 48.53, 48.53, 48.53, 48.53, 48.53, 48.53, 48.53, 48.17, 47.83, 47.83, 46.47, 46.47, 46.47, 48.13, 48.13, 49.1, 49.1, 49.1, 49.1, 49.1, 49.1, 49.1, 49.1, 46.97, 46.97, 46.97, 46.2, 46.2, 46.07, 46.07, 46.6, 46.6, 48.53, 48.53, 48.53, 47.27, 47.27, 47.27, 47.27, 48.43, 48.57, 47.97, 47.97, 47.97, 47.97, 47.97, 47.97, 47.43, 47.43, 47.07, 46.2, 46.2, 46.2, 48.0, 47.23, 47.03, 47.77, 46.97, 47.3, 47.3, 47.4, 47.4, 48.23, 48.23, 47.73, 47.73, 47.73, 47.73, 47.73, 47.73, 49.4, 49.4, 49.4, 47.43, 47.43, 47.43, 47.43, 47.43, 47.43, 45.2, 45.2, 45.2, 46.47, 46.47, 46.47, 46.47, 47.07, 47.07, 47.07, 47.07, 47.13, 48.3, 48.3, 48.0, 47.53, 47.53, 47.53, 47.53, 47.53, 47.5, 47.43, 47.3, 47.3, 46.83, 46.83, 46.83, 46.83, 46.83, 47.53, 46.2, 46.2, 46.2, 46.2, 46.2, 46.2, 46.2, 47.97, 47.97, 47.97, 47.97, 46.67, 46.67, 47.53, 47.53, 47.53, 46.93, 46.93, 46.93, 48.73, 48.73, 48.73, 46.63, 46.63, 46.63, 46.63, 46.63, 46.63, 46.63, 48.67, 49.0, 49.0, 47.7, 47.7, 46.0, 46.0, 46.53, 46.53, 46.13, 46.8, 46.8, 45.77, 45.77, 45.77, 46.03, 46.03, 46.03, 46.03, 46.27]
fed_ecsign_ddos095 = [24.33, 29.73, 32.7, 36.17, 40.73, 43.1, 44.17, 45.0, 47.63, 48.9, 49.7, 50.53, 50.63, 50.13, 50.5, 50.67, 50.27, 50.57, 50.77, 50.17, 50.7, 49.93, 49.5, 50.1, 50.53, 50.27, 49.9, 49.3, 50.43, 49.4, 49.77, 49.33, 49.1, 49.2, 49.13, 49.57, 49.17, 48.73, 48.5, 49.1, 49.27, 48.77, 48.5, 49.1, 49.37, 48.93, 48.67, 48.53, 48.53, 48.4, 47.67, 48.53, 48.2, 48.0, 47.47, 47.77, 46.73, 47.5, 47.67, 47.87, 47.3, 46.67, 48.5, 48.13, 47.8, 47.53, 48.1, 48.03, 46.6, 47.87, 47.03, 46.83, 47.2, 47.57, 47.3, 47.57, 47.6, 47.8, 47.1, 47.2, 47.17, 46.4, 45.53, 47.17, 47.13, 47.13, 47.97, 47.93, 46.87, 46.67, 47.1, 47.13, 46.63, 46.17, 46.7, 46.27, 46.53, 46.7, 46.5, 46.5, 46.5, 46.97, 47.23, 47.33, 47.4, 47.5, 47.93, 47.93, 47.83, 47.67, 47.67, 47.63, 47.83, 47.5, 47.8, 47.93, 48.0, 48.33, 48.2, 48.3, 48.27, 47.8, 47.77, 47.97, 47.7, 47.73, 47.97, 47.87, 47.8, 47.77, 48.13, 47.83, 48.3, 47.97, 48.0, 48.27, 47.97, 48.47, 47.83, 47.9, 48.03, 47.97, 48.33, 48.17, 49.0, 47.8, 48.2, 48.07, 47.77, 48.03, 48.03, 48.2, 48.17, 48.17, 48.1, 48.07, 48.07, 48.07, 48.1, 48.07, 48.03, 48.07, 48.07, 48.07, 48.07, 48.07, 48.13, 48.13, 48.1, 48.1, 48.1, 48.1, 48.07, 48.03, 48.07, 48.07, 48.07, 48.1, 48.1, 48.07, 48.07, 48.1, 48.1, 48.07, 48.07, 48.07, 48.07, 48.07, 48.1, 48.0, 47.97, 48.0, 48.0, 48.03, 48.03, 48.0, 48.0, 48.03, 48.03, 48.07]
fed_efsign_ddos095 = [10.8, 23.77, 30.23, 33.97, 35.83, 37.53, 40.73, 42.37, 46.4, 47.6, 49.6, 49.67, 48.6, 48.23, 48.5, 46.47, 46.67, 47.53, 48.63, 47.37, 48.4, 48.07, 48.47, 48.3, 48.2, 48.23, 48.43, 47.4, 47.67, 47.13, 47.97, 48.37, 47.37, 47.07, 47.6, 47.23, 46.93, 46.37, 46.43, 47.1, 47.87, 47.17, 48.0, 47.3, 46.07, 46.4, 47.3, 46.33, 46.53, 46.87, 47.03, 46.27, 45.4, 45.03, 45.43, 46.27, 44.67, 45.3, 45.8, 45.77, 45.67, 45.63, 44.93, 44.93, 45.5, 45.67, 46.17, 44.13, 45.4, 45.47, 45.23, 45.23, 44.83, 44.5, 45.3, 44.6, 45.77, 44.63, 45.0, 45.13, 43.93, 44.43, 44.67, 44.53, 44.17, 43.37, 45.2, 45.57, 44.2, 44.27, 43.3, 43.8, 44.5, 44.43, 44.13, 42.07, 44.77, 42.27, 44.1, 42.33, 43.63, 44.6, 42.93, 42.8, 43.4, 43.4, 43.33, 43.0, 44.6, 42.93, 44.0, 42.37, 44.47, 42.47, 44.57, 42.17, 44.6, 41.2, 44.13, 42.1, 44.17, 41.97, 44.67, 42.8, 43.2, 40.93, 44.33, 42.4, 43.73, 42.93, 43.6, 41.8, 42.9, 42.47, 43.13, 42.5, 43.7, 44.1, 42.63, 43.73, 44.13, 43.2, 43.37, 42.43, 43.17, 41.83, 43.07, 41.87, 42.6, 42.97, 43.9, 42.23, 42.27, 41.23, 42.03, 40.3, 44.3, 41.57, 41.9, 42.9, 42.9, 42.1, 42.6, 42.87, 42.2, 42.67, 41.97, 40.83, 43.2, 41.27, 42.4, 41.3, 41.73, 42.4, 41.17, 41.73, 43.53, 41.53, 43.47, 41.3, 41.47, 43.6, 41.9, 42.57, 42.47, 41.63, 41.3, 42.83, 41.63, 41.83, 41.37, 41.63, 40.57, 39.37, 42.83, 41.0, 42.17, 40.1, 40.53, 40.97]
fed_mvsign_ddos095 = [22.6, 28.37, 34.8, 39.73, 43.6, 46.7, 47.57, 48.13, 47.57, 48.7, 49.43, 49.3, 50.07, 50.07, 50.0, 49.87, 49.63, 50.07, 50.87, 50.17, 50.63, 51.6, 51.0, 50.27, 50.1, 50.3, 50.13, 50.13, 50.77, 50.47, 50.63, 50.37, 49.97, 49.9, 49.6, 49.5, 49.97, 49.73, 49.4, 50.27, 49.77, 50.5, 49.33, 49.67, 49.03, 49.1, 49.17, 49.67, 49.87, 48.2, 47.73, 47.93, 48.03, 48.1, 48.2, 47.73, 47.37, 48.2, 48.4, 48.07, 47.3, 47.8, 48.07, 47.37, 48.13, 46.6, 47.5, 47.87, 48.77, 48.63, 47.73, 47.57, 46.83, 47.2, 47.27, 47.83, 47.23, 48.1, 48.1, 47.77, 47.47, 47.47, 46.9, 47.07, 46.37, 46.07, 46.03, 46.2, 46.53, 46.6, 46.53, 47.13, 46.57, 47.53, 47.23, 46.83, 46.47, 46.7, 46.83, 47.03, 46.97, 47.1, 46.93, 47.23, 47.63, 47.63, 47.57, 47.8, 47.8, 47.87, 47.77, 47.8, 47.87, 47.93, 48.13, 48.03, 47.87, 48.03, 47.8, 47.67, 47.8, 47.83, 47.97, 47.9, 48.07, 47.7, 47.9, 47.7, 47.9, 48.3, 47.97, 48.3, 47.83, 48.23, 47.87, 47.8, 48.07, 48.03, 48.1, 48.03, 47.93, 48.03, 48.0, 47.77, 47.53, 47.27, 48.0, 47.33, 48.0, 47.87, 47.97, 47.93, 47.8, 47.9, 47.83, 47.87, 47.87, 47.9, 48.03, 48.1, 48.1, 48.07, 47.97, 47.93, 47.93, 47.93, 47.9, 47.87, 47.87, 47.87, 47.8, 47.8, 47.77, 47.77, 47.77, 47.73, 47.7, 47.73, 47.67, 47.67, 47.7, 47.67, 47.67, 47.73, 47.73, 47.77, 47.77, 47.77, 47.83, 47.83, 47.83, 47.8, 47.8, 47.77, 47.77, 47.77, 47.77, 47.77, 47.73, 47.67]
fed_rlrsign_ddos095 = [24.43, 30.0, 33.0, 36.1, 39.07, 40.7, 41.37, 41.9, 42.9, 43.57, 43.1, 42.33, 41.33, 40.47, 40.9, 41.7, 41.03, 40.73, 40.3, 39.47, 37.77, 37.3, 37.97, 39.13, 40.53, 40.13, 39.77, 38.1, 37.8, 37.1, 35.97, 36.63, 37.17, 37.7, 38.13, 38.27, 37.3, 36.57, 37.47, 36.0, 36.4, 35.63, 36.17, 35.37, 34.9, 34.03, 35.53, 36.23, 35.77, 36.7, 35.6, 35.53, 35.1, 35.7, 35.07, 35.17, 34.8, 35.5, 35.13, 36.87, 36.27, 36.23, 35.33, 35.3, 35.37, 35.23, 35.7, 35.7, 35.0, 34.7, 35.23, 34.93, 34.0, 35.1, 35.2, 35.43, 34.8, 35.23, 35.27, 35.33, 34.57, 34.53, 34.73, 34.97, 35.03, 35.07, 35.4, 34.93, 34.43, 36.13, 36.5, 36.13, 35.8, 35.93, 36.37, 35.43, 35.27, 34.07, 33.73, 33.7, 33.5, 33.57, 33.5, 33.5, 33.8, 33.77, 33.53, 33.73, 33.53, 33.43, 33.83, 33.97, 33.8, 34.0, 34.13, 34.2, 34.4, 34.33, 34.6, 34.3, 34.47, 34.2, 34.37, 34.57, 34.5, 34.73, 34.7, 34.57, 34.67, 34.57, 34.77, 35.03, 35.03, 34.8, 35.13, 35.03, 35.1, 35.13, 35.23, 35.07, 35.03, 34.77, 34.53, 34.7, 34.63, 34.8, 34.8, 34.8, 34.93, 34.9, 34.93, 34.87, 34.9, 34.83, 34.87, 34.9, 34.83, 34.87, 34.83, 34.8, 34.8, 34.83, 34.87, 34.9, 34.8, 34.83, 34.8, 34.83, 34.97, 35.0, 34.93, 34.93, 34.93, 34.93, 34.9, 34.9, 34.9, 34.97, 34.97, 34.93, 35.03, 35.03, 34.97, 34.93, 34.93, 34.97, 34.93, 35.0, 35.07, 34.93, 34.9, 34.87, 34.93, 34.9, 34.87, 34.87, 34.83, 34.87, 34.87, 34.93]
fed_sync_sgd_ddos095 = [16.23, 16.83, 28.73, 29.93, 35.33, 37.57, 39.8, 42.5, 43.17, 45.0, 46.1, 46.47, 47.13, 47.73, 47.87, 48.2, 48.43, 48.27, 49.27, 49.03, 49.4, 49.17, 49.03, 48.77, 49.03, 49.03, 49.53, 49.73, 50.1, 49.37, 49.83, 49.73, 49.6, 49.57, 50.0, 50.17, 50.4, 50.4, 50.6, 50.43, 50.43, 49.87, 50.1, 49.87, 50.1, 50.07, 49.8, 50.27, 50.0, 50.03, 49.63, 49.7, 49.6, 49.33, 49.13, 49.53, 49.77, 49.43, 49.63, 49.6, 49.13, 49.33, 49.13, 48.83, 48.8, 49.23, 49.1, 49.5, 49.1, 49.23, 49.2, 49.0, 48.63, 48.4, 48.2, 47.87, 47.6, 47.53, 47.83, 48.07, 48.07, 48.03, 48.13, 48.4, 48.37, 48.1, 48.2, 47.83, 47.7, 48.0, 47.1, 47.2, 46.9, 47.1, 47.03, 46.67, 46.43, 46.47, 46.47, 46.5, 46.43, 46.5, 46.43, 46.63, 46.7, 46.63, 46.7, 46.87, 46.8, 46.83, 46.87, 46.73, 46.83, 46.83, 47.1, 47.2, 47.23, 47.17, 47.17, 47.0, 46.97, 46.97, 46.67, 46.63, 46.77, 46.87, 46.7, 46.8, 46.8, 46.7, 46.67, 46.67, 46.87, 46.77, 46.8, 46.9, 46.63, 46.43, 46.23, 46.1, 46.2, 46.23, 46.4, 46.53, 46.43, 46.63, 46.77, 46.73, 46.63, 46.67, 46.67, 46.63, 46.63, 46.6, 46.6, 46.6, 46.6, 46.6, 46.6, 46.6, 46.6, 46.57, 46.53, 46.53, 46.53, 46.53, 46.53, 46.53, 46.53, 46.53, 46.53, 46.53, 46.53, 46.6, 46.6, 46.6, 46.57, 46.57, 46.57, 46.53, 46.57, 46.57, 46.53, 46.53, 46.53, 46.57, 46.57, 46.57, 46.53, 46.5, 46.5, 46.5, 46.47, 46.47, 46.43, 46.43, 46.43, 46.43, 46.43, 46.43]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc_attack("", fed_sync_sgd_ddos095, fed_ecsign_ddos095, fed_efsign_ddos095, fed_mvsign_ddos095, fed_rlrsign_ddos095, fed_avg_ddos095, save_path, plot_size="3")
