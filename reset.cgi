#!/bin/bash
/usr/bin/mpc -h localhost single off;
/usr/bin/mpc -h localhost repeat off;
/usr/bin/mpc -h localhost clear;
/usr/bin/mpc -h localhost load NameOfPlaylist;
/usr/bin/mpc -h localhost play;
/usr/bin/sleep 0.1;
/usr/bin/mpc -h localhost pause;
