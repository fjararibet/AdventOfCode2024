let rec check_reps a list acc =
  match list with
  | [] -> acc
  | h :: t ->
      let new_acc = if a = h then acc + 1 else acc in
      check_reps a t new_acc

let () =
  let args = Sys.argv in
  let filename = args.(1) in
  let in_channel = open_in filename in
  let rec parse_input acc1 acc2 =
    try
      let line = input_line in_channel in
      let list = List.filter (( <> ) "") (String.split_on_char ' ' line) in
      let [ first; second ] = list in
      parse_input
        (acc1 @ [ int_of_string first ])
        (acc2 @ [ int_of_string second ])
    with End_of_file ->
      close_in in_channel;
      (acc1, acc2)
  in
  let a, b = parse_input [] [] in
  let a = List.sort compare a in
  let b = List.sort compare b in
  let rec result a acc =
      match a with
      | [] -> acc
      | h::t -> let reps = check_reps h b 0 in
      result t (acc + h * reps)
  in
  print_int (result a 0)
