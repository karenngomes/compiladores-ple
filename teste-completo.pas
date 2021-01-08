program teste;
	var entrada, lenght, aux, aux2, pot, output : integer;
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
            aux2 := 0;
            while (aux2 < lenght) do
            begin
                pot := 10*pot;
                aux2 := aux2 + 1;
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