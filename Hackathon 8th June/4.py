# playlist manager
import sys

n = int(sys.stdin.readline())
song_list = list(sys.stdin.readline().split())
k = int(sys.stdin.readline())
mid = n//2

print("Playlist: ", " ".join(song_list))
print("Reversed: ", " ".join(song_list[::-1]))
print("Middle: ", song_list[mid])
print("Kth From End: ", song_list[-k])