with Ada.Text_IO; use Ada.Text_IO;


procedure Main is
   Input_File: File_Type;
   Value     : Character;
   g         : Boolean := False;

begin
   Ada.Text_IO.Open(File => Input_File, Mode => Ada.Text_IO.In_File, Name => "out.txt");
   while not End_Of_File(Input_File) loop
      Ada.Text_IO.get(File => Input_File,
                      Item => Value);

      if(g) then
         Ada.Text_IO.Put(Item => Value);
         Ada.Text_IO.New_Line;
      end if;

      if(Value = '!') then
         g := True;
      end if;

   end loop;
   Ada.Text_IO.close(File => Input_File);
end Main;
