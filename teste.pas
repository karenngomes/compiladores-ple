program teste;
	var entrada, aux, te1 : integer;
			te, ti : boolean;

	procedure umprocedimento(argproc1, argproc2 : integer; argproc3, argproc4 : boolean);
		var procvar, pvar : boolean;
				intprocvar, ppvar : integer;

		procedure outroproc;
			var x : integer;
			begin
				v := 1;
				procvar := procvar + v;
			end;

		procedure maisumproc;
			var x : integer;
			begin
				v := 1;
			end;

		function funcinproc(arg1 : integer; arg2 : boolean) : integer;
		begin
			arg1 := 3;
			arg2 := 0;
		end;

		begin
			procvar := 1;
			intprocvar := 34;
			ppvar := 2 + intprocvar;
			outroproc;
			maisumproc;
		end;

	function umafuncao(funcvar : integer) : integer;
	begin	
		funcvar := 1;
	end;



begin
    entrada := 15 + 15 * 12;
    
	if (entrada > aux) then
    	begin 
        aux := 5;
    	end
	else
		begin
		aux := 10;
		end;

	if (b and y) then
	begin
		x := a + b;
	end;
	
	umprocedimento;

	for entrada := 1 to 5 do
	begin
		read(entrada);
	end;

	while (x < 10) do
	begin
		write(entrada);
	end;
end
.
