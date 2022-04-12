function txtToMat()
    txtPath = 'F:\program\SiamGAT-main\SiamGAT-main\tools\results\LSOTB\checkpoint_e19_SSM_gray\';
    name = dir(txtPath);
    annobegin = 1;
    startFrame = 1;
    type = 'rect';
    len = numel(name)-2;
    fps = 24
    for i=3:numel(name)
        file = name(i).name;
        path = strcat(txtPath,file);
        res = load(path);
        %results = ('res','type','len','annobegin','startFrame','fps')
        save(file,'res','type','len','annobegin','startFrame','fps')
    end
end
