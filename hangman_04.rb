# config: utf-8

$words = ["test", "example", "sample", "work"] # 単語のリスト
$answer = []; #当てられた文字とそうでない部分を覚えておくための配列
$question
$miss = 4 # 新しく付け加えた部分

def select_question
  index = rand($words.length) # 乱数を使って、添字をランダムに選ぶ
  $question = $words[rand($words.length)] # 単語リストから無作為に一つ選び出す
  0.upto($question.length-1){|n|
    $answer[n] = '_' # 配列の全ての要素を’_’にする
  }
end

def q_and_a
  puts("問題：#{$answer}") #配列の要素をまとめて一行に出力
  print("単語に含まれると思う文字を入力してね（あと#{$miss}回間違えられるよ）＞")
  input = gets
  guess = input[0].chr
  puts("あなたの考えは#{guess}ですね。")
  is_found = false 
  #入力された文字が$questionのなかにあったかどうかを記憶する変数
  0.upto($question.length - 1){|n|
    #questionの各文字にguessが含まれているかどうかを調べる
    if $question[n].chr == guess
      $answer[n] = guess
      #もし含まれていたらanswerの同じ部分をguessで置き換える
      is_found = true
      #もし含まれていたらあったことを記憶しておく
    end
  }
  if !is_found
    # 入力された文字が含まれていなかったら、$missの値を減らす。
    $miss -= 1
    puts("残念ながらその文字は含まれていないんだ")
  end
end

select_question
# $answerに'_'が含まれる、そして $missの値が０より大きいときゲームを続ける
while $answer.index('_') != nil && $miss > 0
  q_and_a
end

puts("正解は#{$question}でした。")
if $miss > 0 
  #プレーヤーが勝った場合
  puts("あなたの勝ち。とほほほ。")
else
  #プレーヤーが負けた場合
  puts("やったね。私の勝ち！")
end
