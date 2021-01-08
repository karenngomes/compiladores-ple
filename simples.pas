program simples;
	var entrada, aux : integer;
			a, b : boolean;

begin
    a := 1;
    b := 1;
    write(b);
    repeat
        read(entrada);
        if (a and b) then
        begin
            write(entrada);
            read(a);
        end;
        
    until(a);

end.