def countEmail():
    # This first line is provided for you
    file_name = input("Enter file:")
    if len(file_name) < 1 : file_name = "mbox-short.txt"
    fhand = open(file_name)

    sender_counts = dict()

    for line in fhand:
        words = line.split()
        if len(words) < 2:
            continue
        if words[0] != 'From':
            continue
        #print(line) 
        sender = words[1]
        for word in words:
            if word != sender:
                continue
            sender_counts[word] = sender_counts.get(word,0) + 1

    max_sender = max(sender_counts, key = sender_counts.get)
    max_sender_count = sender_counts[max_sender]
            
    print(max_sender, max_sender_count)
        
## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## countEmail()
