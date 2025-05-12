<?php

while (true) {
    echo "1. Add Contact\n";
    echo "2. View Contacts\n";
    echo "3. Exit\n";
    $choice = readline("Enter your choice: ");

    if ($choice == '1') {
        $input_name = readline("Enter contact name: ");
        $input_phone = readline("Enter phone number: ");
        $dictContact[$input_name] = $input_phone;
        echo "Contact added\n";
        if (count($dictContact) == 3) {
            echo "No more space to add contact!\n";
            break;
        }
    } elseif ($choice == '2') {
        if (!empty($dictContact)) {
            foreach ($dictContact as $input_name => $input_phone) {
                echo "Name: $input_name, Phone: $input_phone\n";
            }
        } else {
            echo "No contacts saved.\n";
        }
    } elseif ($choice == '3') {
        break; // break to exit
    }
}

?>