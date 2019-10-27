import unittest

from create_alias import build_filepath, prepare_alias_statement


class FilepathTests(unittest.TestCase):

    def test_zsh(self):
        shell = "/bin/zsh"
        self.assertEqual("~/.zshrc", build_filepath(shell))

    def test_bash(self):
        shell = "/bin/bash"
        self.assertEqual("~/.bashrc", build_filepath(shell))


class PrepateAliasStatementTests(unittest.TestCase):

    def test_complex_string(self):
        alias = "dev"
        command = "EXPORT KUBECONFIG=~/dev-k8s.yml;SET http_proxy="
        self.assertEqual(
            "alias dev='EXPORT KUBECONFIG=~/dev-k8s.yml;SET http_proxy='\n", prepare_alias_statement(alias, command)
        )
