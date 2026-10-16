{
  description = "Machine Learning Labs - JupyterLab";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};

      pythonEnv = pkgs.python3.withPackages (ps: with ps; [
        jupyterlab
        ipykernel
        numpy
        matplotlib
      ]);
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [ pythonEnv ];

        NIX_DEV_NAME = "ml-labs";

 	shellHook = ''
          PS1="\[\e[1;35m\]($NIX_DEV_NAME)\[\e[0m\] $PS1"
        '';
      };
    };
}

