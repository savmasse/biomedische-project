from sqlConnection import SqlConnection
import tempfile
import os
import pygame
import pygame.mixer as mix

# Handle audio read/write

s = SqlConnection("main.db");
(contentID, content, contentType, category) = s.selectContent("main", 1);

# write the data to a tempfile
new_file, fname = tempfile.mkstemp(suffix = ".mp3");
print (fname);
os.write(new_file, content);

pygame.init();
mix.init();

print(mix.get_init());
screen=pygame.display.set_mode((400,400),0,32) 

mix.music.load("C:\\Users\\SamVa\\Desktop\\UGent\\Biomedische\\test.mp3");
mix.music.play();

while (mix.music.get_busy()):
    print ("Playing");
    pygame.time.Clock().tick(10);

# Close temp file
os.close(new_file);
