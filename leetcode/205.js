// 205. Isomorphic Strings

var isIsomorphic = function(s, t) {
    
    let h = {};
    let h2 = {}
    for ( let i = 0; i < s.length; i++){
        if ( h[s[i]]){
            if (h[s[i]] !== t[i]) return false;
        } else {
            h[s[i]] = t[i];
        }
        if ( h2[t[i]]){
            if (h2[t[i]] !== s[i]) return false;
        } else {
            h2[t[i]] = s[i];
        }
    }
    return true;
    
};
