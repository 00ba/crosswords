# config: utf-8

$words = ["test", "example", "sample", "work"] # 単語のリスト
$answer = []; #当てられた文字とそうでない部分を覚えておくための配列
$question

def select_question
  index = rand($words.length) # 乱数を使って、添字をランダムに選ぶ
  $question = $words[rand($words.length)] # 単語リストから無作為に一つ選び出す
  0.upto($question.length-1){|n|
    $answer[n] = '_' # 配列の全ての要素を’_’にする
  }
end

def q_and_a
  puts("問題：#{$answer}") #配列の要素をまとめて一行に出力
  print("単語に含まれると思う文字を入力してね＞")
  input = gets
  guess = input[0].chr
  puts("あなたの考えは#{guess}ですね。")
  0.upto($question.length - 1){|n|
    if $question[n].chr == guess
      $answer[n] = guess
    end
  }
end

select_question
q_and_a
