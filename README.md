## goit-algo-hw-06
**Опис:**
Для аналізу я обрав центральну частину Київського метро:
![Центральна частина київського метро](https://github.com/Spogoretskyi/goit-algo-hw-06/blob/main/images/kyiv_metro.png)
# Отримано наступні результати:

# Завдання 1:
Кількість вершин: 25<br>
Кількість ребер: 25<br>
| Станція                                                                                    | Ступінь вершини     | 
|--------------------------------------------------------------------------------------------|---------------------|
| Khreshchatyk, Palats Sportu, Zoloti Vorota, Maidan Nezalezhnosti, Teatralna, Lva Tolstogo  |  3                  |
| Arsenalna, Poshtova Ploscha, Lukiyanivska, Klovska, Pecherska, Druzhby Narodiv, Vydubichy, |  2                  |
| Olimpiyska, Vokzalna, Universytet, Palats Ukraina, Slavutych, Kontraktova Ploscha          |  2                  |
| Shuliavska, Hidropark, Plosha Tarasa Shevchenka, Lybidska, Osokorky, Dorogozhychy          |  1                  |

# Завдання 2:
Я вирышив порівняти шлях `Dorogozhychy` ---> `Vokzalna`<br>
Отриманий шлях використовуючи алгоритм 'dfs':<br>
[['Dorogozhychy', 'Lukiyanivska', 'Zoloti Vorota', 'Palats Sportu', 'Lva Tolstogo', 'Maidan Nezalezhnosti', 'Khreshchatyk', 'Teatralna', 'Universytet', 'Vokzalna'], ['Dorogozhychy', 'Lukiyanivska', 'Zoloti Vorota', 'Teatralna', 'Universytet', 'Vokzalna']]<br>

Отриманий шлях використовуючи рекурсивний алгоритм 'bfs':<br>
[['Dorogozhychy', 'Lukiyanivska', 'Zoloti Vorota', 'Teatralna', 'Universytet', 'Vokzalna'], ['Dorogozhychy', 'Lukiyanivska', 'Zoloti Vorota', 'Palats Sportu', 'Lva Tolstogo', 'Maidan Nezalezhnosti', 'Khreshchatyk', 'Teatralna', 'Universytet', 'Vokzalna']]<br>

# Висновок:
Як бачимо отримані шляхи відрізняються і ми бачему, що у конкретному випадку `DFS (Depth-First Search)` виявився трохи ефективнішим 16 VS 17, але потрібно розуміти, що це конкретний випадок, зазвичай для пошуку маршруту `BFS (Breadth-First Search)` може працювати ефективніше:    
`DFS (Depth-First Search)` вибирає один із шляхів і досліджує його глибше, перш ніж переходити до інших шляхів. Тому шляхи, знайдені DFS, можуть бути менш оптимальними, але алгоритм працює швидше.<br>
`BFS (Breadth-First Search)` досліджує всі можливі шляхи на одному рівні, перш ніж переходити на наступний рівень. Це може привести до знаходження оптимальних шляхів, але алгоритм може бути менш ефективним в розрахунках за DFS.<br>

також можна порівняти графічно ці два алгоритми:<br>
**DFS**
![dfs](https://github.com/Spogoretskyi/goit-algo-hw-06/blob/main/images/dfs.png)
**BFS**
![bfs](https://github.com/Spogoretskyi/goit-algo-hw-06/blob/main/images/bfs.png)



