## goit-algo-hw-06
# Опис:
Для аналізу я обрав центральну частину Київського метро:


# Отримано наступні результати:

# Завдання 1:
Кількість вершин: 25<br>
Кількість ребер: 25<br>

Ступінь кожної вершини:<br>
Shuliavska: 1<br>
Vokzalna: 2<br>
Universytet: 2<br>
Teatralna: 3<br>
Khreshchatyk: 3<br>
Arsenalna: 2<br>
Hidropark: 1<br>
Maidan Nezalezhnosti: 3<br>
Poshtova Ploscha: 2<br>
Kontraktova Ploscha: 2<br>
Plosha Tarasa Shevchenka: 1<br>
Lva Tolstogo: 3<br>
Olimpiyska: 2<br>
Palats Ukraina: 2<br>
Lybidska: 1<br>
Osokorky: 1<br>
Slavutych: 2<br>
Vydubichy: 2<br>
Druzhby Narodiv: 2<br>
Pecherska: 2<br>
Klovska: 2<br>
Palats Sportu: 3<br>
Zoloti Vorota: 3<br>
Lukiyanivska: 2<br>
Dorogozhychy: 1<br>

# Завдання 2:
Я вирышив порівняти шлях "Dorogozhychy" ---> "Vokzalna"<br>
Отриманий шлях використовуючи алгоритм 'dfs':<br>
[['Dorogozhychy', 'Lukiyanivska', 'Zoloti Vorota', 'Palats Sportu', 'Lva Tolstogo', 'Maidan Nezalezhnosti', 'Khreshchatyk', 'Teatralna', 'Universytet', 'Vokzalna'], ['Dorogozhychy', 'Lukiyanivska', 'Zoloti Vorota', 'Teatralna', 'Universytet', 'Vokzalna']]<br>

Отриманий шлях використовуючи рекурсивний алгоритм 'bfs':<br>
[['Dorogozhychy', 'Lukiyanivska', 'Zoloti Vorota', 'Teatralna', 'Universytet', 'Vokzalna'], ['Dorogozhychy', 'Lukiyanivska', 'Zoloti Vorota', 'Palats Sportu', 'Lva Tolstogo', 'Maidan Nezalezhnosti', 'Khreshchatyk', 'Teatralna', 'Universytet', 'Vokzalna']]<br>

# Висновок:
Як бачимо отримані шляхи відрізняються і ми бачему, що у конкретному випадку 'DFS (Depth-First Search)' виявився трохи ефективнішим 16 VS 17, але потрібно розуміти, що це конкретний випадок, зазвичай для пошуку маршруту 'BFS (Breadth-First Search)' може працювати ефективніше:    
'DFS (Depth-First Search)' вибирає один із шляхів і досліджує його глибше, перш ніж переходити до інших шляхів. Тому шляхи, знайдені DFS, можуть бути менш оптимальними, але алгоритм працює швидше.<br>
'BFS (Breadth-First Search)' досліджує всі можливі шляхи на одному рівні, перш ніж переходити на наступний рівень. Це може привести до знаходження оптимальних шляхів, але алгоритм може бути менш ефективним в розрахунках за DFS.<br>


