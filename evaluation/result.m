function makeFile()
    path = 'F:\program\PTB-TIR_Evaluation_toolkit-master\PTB-TIR_Evaluation_toolkit-master\perfMat\Overall_all\temp\';
    name = dir(path);
    
    for i=3:numel(name)
        mat_name = name(i).name;
        str = strcat(path,mat_name);
        results = load(str);
        results.len = numel(results.res)/4;
        save(mat_name,'results');
    end
end