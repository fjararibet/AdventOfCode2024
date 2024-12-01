let () = 
    let args = Sys.argv in
    let filename = args.(1) in
    let in_channel = open_in filename in
    let rec parse_input acc1 acc2 = 
        try
            let line = input_line in_channel in
            let list = List.filter ((<>) "") (String.split_on_char ' ' line) in
            let first :: second :: [] =  list in
            parse_input (acc1 @ [int_of_string first]) (acc2 @ [int_of_string second])
        with
        | End_of_file ->
                close_in in_channel;
                acc1, acc2
    in
    let a, b = parse_input [] [] in
    let a = List.sort compare a in
    let b = List.sort compare b in
    let rec result a b acc =
        match a, b with
        | [], [] -> acc
        | h1::t1, h2::t2 -> result t1 t2 (acc + abs (h1 - h2))
        | _ -> failwith "imp"
    in
    print_int (result a b 0)

