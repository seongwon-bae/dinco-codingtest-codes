def get_melon_best_album(genre_array, play_array):
    # 장르의 총합을 각각 구해서 딕셔너리에 삽입 [장르 : [총합, {인덱스: 횟수}]]로 정리
    genre_dict = {}
    for i in range(len(genre_array)):
        if genre_dict.get(genre_array[i]) == None:
            genre_dict[genre_array[i]] = [play_array[i], {i: play_array[i]}]
        else:
            genre_dict[genre_array[i]][0] += play_array[i]
            genre_dict[genre_array[i]][1][i]=play_array[i]
    sorted_genre = sorted(genre_dict.items(), key=lambda x:x[1][0], reverse=True)
    answer = []
    for item in sorted_genre:
        answer.extend([index for index,_ in sorted(item[1][1].items(), key=lambda x:x[1], reverse=True)][:2])
    return answer


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))