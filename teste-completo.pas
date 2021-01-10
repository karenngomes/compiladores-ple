program teste;
	var entrada, lenght, aux, count, pot, output : integer;
			isover, print : boolean;

    

begin
	read(entrada);
    aux := 0;
    isover := 0;
    print := 1;

    while (not isover and print) do
    begin
        lenght := 0;
        output := 0;
        repeat
            pot := 1;
            for count := 0 to lenght - 1 do
            begin
                pot := pot * 10;
            end;

            output := pot*entrada + output;
            lenght := lenght + 1;
        until (lenght > aux);
        
        write(output);
        aux := aux + 1;

        if (aux >= entrada) then
        begin
            isover := 1;
        end;        
    end;

end.