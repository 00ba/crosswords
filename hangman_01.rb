# config: utf-8
words = ["test", "example", "sample","work"] # 単語の集まり
index = rand(words.length) # 乱数を使って、添字をランダムに選ぶ
question = words[index] # 単語の集まりからランダムに一つ選び出す
puts(question) # 選んだ単語を出力する