<?php

function run_quiz(array $questions): float
{
    $score = 0;

    foreach ($questions as $quiz => $answer) {
        $guess = readline("$quiz: ");
        if (strtolower($guess) == strtolower($answer)) {
            echo "Correct!" . PHP_EOL;
            $score++;
        } else {
            echo "Incorrect. The correct answer is $answer." . PHP_EOL;
        }

        echo "\n";
    }

    echo "\nYou got $score out of " . count($questions) . " questions correct." . PHP_EOL;
    return ($score / count($questions)) * 100;
}

$questions = [
    "How many legs does a spider have?" => "8",
    "How many total days in a year??" => "365",
    "How many colors in a rainbow?" => "7"
];

$percentage = run_quiz($questions);
echo "Your score is " . number_format($percentage, 2) . "%." . PHP_EOL;

?>