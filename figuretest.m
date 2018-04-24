xg = '/Users/zhengwei/Desktop/data/Normal_X_Gyroscope.csv';
X_G = xlsread(xg);
yg = '/Users/zhengwei/Desktop/data/Normal_Y_Gyroscope.csv';
Y_G = xlsread(yg);
zg = '/Users/zhengwei/Desktop/data/Normal_Z_Gyroscope.csv';
Z_G = xlsread(zg);
xa = '/Users/zhengwei/Desktop/data/Normal_X_Accelerometer.csv';
X_A = xlsread(xa);
ya = '/Users/zhengwei/Desktop/data/Normal_Y_Accelerometer.csv';
Y_A = xlsread(ya);
za = '/Users/zhengwei/Desktop/data/Normal_Z_Accelerometer.csv';
Z_A = xlsread(za);
k = 1:80;

figure(1);
plot(k,X_G(430,:),'r');
hold on;
plot(k,X_G(431,:),'b');
hold on;
plot(k,X_G(432,:),'g');
hold on;
xlabel('time/20ms');
ylabel('Accelerometer');
title('sitdown X_G');
saveas(gcf,'/Users/zhengwei/Desktop/sitdown_XG.png');

figure(2);
plot(k,Y_A(430,:),'r');
hold on;
plot(k,Y_A(431,:),'b');
hold on;
plot(k,Y_A(432,:),'g');
hold on;
xlabel('time/20ms');
ylabel('Accelerometer');
title('sitdown Y_A');
saveas(gcf,'/Users/zhengwei/Desktop/sitdown_YA.png');

figure(3);
plot(k,Z_A(430,:),'r');
hold on;
plot(k,Z_A(431,:),'b');
hold on;
plot(k,Z_A(432,:),'g');
hold on;
xlabel('time/20ms');
ylabel('Accelerometer');
title('sitdown Z_A');
saveas(gcf,'/Users/zhengwei/Desktop/sitdown_ZA.png');

% figure(1);
% plot(k,X_A(4,:),'r');
% hold on;
% plot(k,X_A(5,:),'b');
% hold on;
% plot(k,X_A(6,:),'g');
% hold on;
% xlabel('time/20ms');
% ylabel('Accelerometer');
% title('Fall X_A');
% saveas(gcf,'/Users/zhengwei/Desktop/Fall_XA.png');

% figure(2);
% plot(k,X_A(11,:),'r');
% hold on;
% plot(k,X_A(12,:),'b');
% hold on;
% plot(k,X_A(13,:),'g');
% hold on;
% xlabel('time/20ms');
% ylabel('Accelerometer');
% title('Walk X_A');
% saveas(gcf,'/Users/zhengwei/Desktop/Walk_XA.png');


% figure(4);
% plot(k,X_G(11,:),'r');
% hold on;
% plot(k,X_G(12,:),'b');
% hold on;
% plot(k,X_G(13,:),'g');
% hold on;
% xlabel('time/20ms');
% ylabel('Accelerometer');
% title('Walk X_G');
% saveas(gcf,'/Users/zhengwei/Desktop/Walk_XG.png');


% figure(6);
% plot(k,Y_A(11,:),'r');
% hold on;
% plot(k,Y_A(12,:),'b');
% hold on;
% plot(k,Y_A(13,:),'g');
% hold on;
% xlabel('time/20ms');
% ylabel('Accelerometer');
% title('Walk Y_A');
% saveas(gcf,'/Users/zhengwei/Desktop/Walk_YA.png');

% figure(7);
% plot(k,Y_G(4,:),'r');
% hold on;
% plot(k,Y_G(5,:),'b');
% hold on;
% plot(k,Y_G(6,:),'g');
% hold on;
% xlabel('time/20ms');
% ylabel('Accelerometer');
% title('Fall Y_G');
% saveas(gcf,'/Users/zhengwei/Desktop/Fall_YG.png');
% 
% figure(8);
% plot(k,Y_G(11,:),'r');
% hold on;
% plot(k,Y_G(12,:),'b');
% hold on;
% plot(k,Y_G(13,:),'g');
% hold on;
% xlabel('time/20ms');
% ylabel('Accelerometer');
% title('Walk Y_G');
% saveas(gcf,'/Users/zhengwei/Desktop/Walk_YG.png');



% figure(10);
% plot(k,Z_A(11,:),'r');
% hold on;
% plot(k,Z_A(12,:),'b');
% hold on;
% plot(k,Z_A(13,:),'g');
% hold on;
% xlabel('time/20ms');
% ylabel('Accelerometer');
% title('Walk Z_A');
% saveas(gcf,'/Users/zhengwei/Desktop/Walk_ZA.png');
% 
% figure(11);
% plot(k,Z_G(4,:),'r');
% hold on;
% plot(k,Z_G(5,:),'b');
% hold on;
% plot(k,Z_G(6,:),'g');
% hold on;
% xlabel('time/20ms');
% ylabel('Accelerometer');
% title('Fall Z_G');
% saveas(gcf,'/Users/zhengwei/Desktop/Fall_ZG.png');
% 
% figure(12);
% plot(k,Z_G(11,:),'r');
% hold on;
% plot(k,Z_G(12,:),'b');
% hold on;
% plot(k,Z_G(13,:),'g');
% hold on;
% xlabel('time/20ms');
% ylabel('Accelerometer');
% title('Walk Z_G');
% saveas(gcf,'/Users/zhengwei/Desktop/Walk_ZG.png');