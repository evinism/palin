rm -rf data
mkdir data
cd data
curl http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip --output twitter.zip
unzip twitter.zip
cd ../
cat data/Sentiment\ Analysis\ Dataset.csv | python prettify_data.py > data/positive.txt
cat data/positive.txt | python randomize_word_order.py > data/negative.txt
#python palin.py | head -$(wc -l < data/positive.txt | sed -e "s/ //g") > data/negative.txt
