program teste;
	var entrada, aux : integer;
			a, b : boolean;

begin
	entrada := 10;
  aux := 1;
  while (aux <= 10) do
    begin
      if (entrada > aux) then
        begin
          write(aux);
        end
      else
        begin
          write(entrada);
        end;
        aux := aux + 1;
    end;
end.