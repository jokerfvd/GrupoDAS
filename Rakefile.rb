desc "Print teste."
task :test do
  puts "Teste"
end

task :default => [:test]