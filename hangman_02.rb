words = ["test", "example", "sample", "work"] # 単語のリスト
index = rand(words.length) # 乱数を使って、添字をランダムに選ぶ
question = words[rand(words.length)] # 単語リストから無作為に一つ選び出す
answer = []; #当てられた文字とそうでない部分を覚えておくための配列
puts(question) # 選んだ単語を出力する
0.upto(question.length-1){|n|
  answer[n] = '_' # 配列の全ての要素を’_’にする
}
puts("単語を当ててね。")
puts("問題：#{answer}") #配列の要素をまとめて一行に出力
print("単語に含まれると思う文字を入力してね＞")
input = gets
puts("あなたの考えは#{input}ですね。")