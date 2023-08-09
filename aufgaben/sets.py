report = '''Die Editionswissenschaft erlebt nicht zuletzt wegen einer 
            erfolgreichen Kombination von traditionellen Arbeitsweisen 
            mit Methoden der Digital Humanities einen regelrechten Hype. 
            Digitale Methoden drängen sich besonders an den Stellen auf, 
            wo sie eine Überwindung der Beschränkungen des analogen Drucks versprechen. 
            Zugleich zeichnet sich ab, dass mit einem Wechsel zu digitalen Editionsformen 
            nicht nur neue Werkzeuge genutzt werden, sondern dass sich prinzipielle 
            strukturelle Änderungen ergeben: so können analoge Editionen angereichert 
            werden oder Editionen können als Hybrid durch eine gleichwertige digitale und 
            analoge Version repräsentiert werden. Editoren werden angesichts dieser neuen
            Möglichkeiten vor neue Herausforderungen gestellt. Gleiches gilt für Infrastrukturen, 
            die die Produkte der Editionswissenschaft publizieren und langfristig 
            verfügbar machen sollen. Grundlegende Fragen der Qualitätsmessung 
            und -bewertung, der Arbeitsorganisation, Vernetzung und Distribution 
            müssen bei der digitalen Editionswissenschaft anders bzw. neu gestellt 
            und bewertet werden. Die vom Forschungsverbund Marbach Weimar Wolfenbüttel 
            veranstaltete Tagung “Digitale Metamorphose: Digital Humanities und Editionswissenschaft” 
            betrachtete diese neuen Möglichkeiten kritisch und ging dabei auch der Frage nach, 
            welche Grenzen und Gefahren es jenseits der offensichtlichen Vorteile für 
            die Editionswissenschaft gibt.'''

# split text into list of words
tokenized_report = report.split()

# compute and print length of report
print(f'''Der Tagungsbericht "Digitale Metamorphose. Digital Humanities und Editionswissenschaft" 
enthält insgesamt {len(tokenized_report)} Wörter.''')

# transform list into set
unique_words_report = set(tokenized_report)

# compute and print length of set
print(f'''Der Tagungsbericht "Digitale Metamorphose. Digital Humanities und Editionswissenschaft" 
enthält {len(unique_words_report)} verschiedene Wörter.''')

# print set
print(unique_words_report)