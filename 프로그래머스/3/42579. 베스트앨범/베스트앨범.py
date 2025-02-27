def solution(genres, plays):
    answer = []
    songs_genre = {}
    songs_plays = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in songs_plays:
            songs_plays[genre] = 0
            songs_genre[genre] = []
        
        songs_plays[genre] += play
        songs_genre[genre].append((play, i))
        
    sorted_genres = sorted(songs_plays.keys(), 
                          key=lambda x: songs_plays[x], 
                          reverse=True)
    
    for genre in songs_genre:
        songs_genre[genre].sort(key=lambda x: (-x[0], x[1]))
        
    for genre in sorted_genres:
        num = min(2, len(songs_genre[genre]))
        for i in range(num):
            answer.append(songs_genre[genre][i][1])
            
    return answer