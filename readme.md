# Word Frequency Lists

The most frequently used 5,000 words in English, French, and Spanish, plus Chinese character frequency lists.

---

## English (`en/`)

| #   | Source                                                                                                                       | File                      | Status   | Notes                                                            |
| --- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------- | -------- | ---------------------------------------------------------------- |
| 1   | [TV and Movie Scripts (2006)](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/English/TV_and_Movie_Scripts_(2006)) | ~~tv.txt~~                | Removed  | Contains patterns like "Ivy or ivy" as one entry, and like "W ." |
| 2   | [Wikipedia (2016)](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/English/Wikipedia_(2016))                       | [wiki.txt](en/wiki.txt)   | Included | Contains multi-word phrases like "the most" as single entries    |
| 3   | [hermitdave FrequencyWords](https://github.com/hermitdave/FrequencyWords/blob/master/content/2018/en/en_50k.txt)             | [en_5k.txt](en/en_5k.txt) | ✅ Good   | **License:** CC BY-SA 4.0                                        |

> Source #2 is based on: D. Goldhahn, T. Eckart & U. Quasthoff. "Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages." *Proceedings of the 8th International Language Resources and Evaluation (LREC'12)*, 2012.

---

## French (`fr/`)

| #   | Source                                                                                                             | File                                                | Status   | Notes                                                                     |
| --- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------- | -------- | ------------------------------------------------------------------------- |
| 1   | [Lexique 4](http://www.lexique.org/?page_id=790&lang=en)                                                           | [lexique4_5000.tsv](fr/lexique4_5000.tsv)           | ✅ Good   | Generated via `code/lexique4.sql`. Has attributes. **License:** CC BY-SA  |
| 2   | [OpenSubtitles 5000](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/French_wordlist_opensubtitles_5000) | [opensubtitles_5000.txt](fr/opensubtitles_5000.txt) | Included | Based on movie subtitles from opensubtitles.org, compiled by User:Hermitd |

> Source #1 is based on: New, B., Pallier, C., Schalchli, G., Bourgin, J., & Gimenes, M. (2026). "Lexique 4: A major upgrade of the 'Lexique' French lexical database." *Behavior Research Methods*.

---

## Spanish (`es/`)

| #   | Source                                                                                                           | File                                  | Status   | Notes                                                                                                                                                                   |
| --- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | [Mixed 730K](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish/Mixed_730K)                       | [mix_730k.txt](es/mix_730k.txt)       | Included | Contains multi-word phrases. Based on Wortschatz Leipzig 2021 Wikipedia & 2022 News 1M Sentence corpora                                                                 |
| 2   | [Subtitles 10K](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish/Subtitles10K) (5 parts)        | [subtitles5k.txt](es/subtitles5k.txt) | ✅ Good   | Combined from raw files in `es/subtitles5k_raw/` via `code/combine_spannish.py`. ~27.4 million words from movie/TV subtitles. Has lemma forms. **License:** GFDL & LGPL |
| 3   | [hermitdave FrequencyWords](https://github.com/hermitdave/FrequencyWords/blob/master/content/2018/es/es_50k.txt) | [es_5k.txt](es/es_5k.txt)             | Included | **License:** CC BY-SA 4.0                                                                                                                                               |

<details>
<summary>Subtitles raw source links (source #2)</summary>

- [Spanish 1000](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish1000)
- [Spanish 1001–2000](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish1001-2000)
- [Spanish 2001–3000](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish2001-3000)
- [Spanish 3001–4000](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish3001-4000)
- [Spanish 4001–5000](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish4001-5000)

</details>

> Source #1 is based on: D. Goldhahn, T. Eckart & U. Quasthoff. "Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages." *Proceedings of the 8th International Language Resources and Evaluation (LREC'12)*, 2012.

---

## Chinese (`zh/`)

| #   | Source                                                                                                                      | File                                    | Status   | Notes                                                                                                                       |
| --- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1   | [BLCU 25亿字语料汉字字频表](https://faculty.blcu.edu.cn/xinghb/zh_CN/article/167473/content/1437.htm#article) by 邢红兵     | [blcu_5000.csv](zh/blcu_5000.csv)       | Included | 仅供研究者进行汉字及相关研究之用 (for research use only)                                                                    |
| 2   | [MTSU 汉字单字字频总表](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=TO) by 笪骏                | [mtsu_5000.tsv](zh/mtsu_5000.tsv)       | Included | Combined Classical and Modern Chinese. For research/teaching only; commercial use requires written permission               |
| 3   | [通用规范汉字表 (一级字表)](https://zh.wikisource.org/wiki/%E9%80%9A%E7%94%A8%E8%A7%84%E8%8C%83%E6%B1%89%E5%AD%97%E8%A1%A8) | [hanzi_1_3500.txt](zh/hanzi_1_3500.txt) | ✅ Good   | 3,500 most common simplified Chinese characters (not ordered by frequency). Issued by State Council notice 国发〔2013〕23号 |

> Source #3: 根据2013年6月18日《国务院关于公布〈通用规范汉字表〉的通知》（国发〔2013〕23号）印发 原文件.


---


## Code

- `code/lexique4.sql` — Generates `fr/lexique4_5000.tsv` from the Lexique 4 database
- `code/combine_spannish.py` — Combines raw Spanish subtitle files into `es/subtitles5k.txt`
