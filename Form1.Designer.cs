namespace getmem_gui
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dumpsys_meminfo = new System.Windows.Forms.Button();
            this.meminfo = new System.Windows.Forms.TextBox();
            this.pid = new System.Windows.Forms.Label();
            this.inputPID = new System.Windows.Forms.TextBox();
            this.getmem = new System.Windows.Forms.Button();
            this.phone_state = new System.Windows.Forms.TextBox();
            this.button_phone = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.button_analysis = new System.Windows.Forms.Button();
            this.result = new System.Windows.Forms.TextBox();
            this.button_result = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.keyword_search = new System.Windows.Forms.TextBox();
            this.search = new System.Windows.Forms.Button();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.button_savedir = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // dumpsys_meminfo
            // 
            this.dumpsys_meminfo.Location = new System.Drawing.Point(499, 38);
            this.dumpsys_meminfo.Name = "dumpsys_meminfo";
            this.dumpsys_meminfo.Size = new System.Drawing.Size(106, 23);
            this.dumpsys_meminfo.TabIndex = 0;
            this.dumpsys_meminfo.Text = "内存信息";
            this.dumpsys_meminfo.UseVisualStyleBackColor = true;
            this.dumpsys_meminfo.Click += new System.EventHandler(this.button1_Click);
            // 
            // meminfo
            // 
            this.meminfo.AcceptsReturn = true;
            this.meminfo.AcceptsTab = true;
            this.meminfo.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.meminfo.Location = new System.Drawing.Point(15, 77);
            this.meminfo.Multiline = true;
            this.meminfo.Name = "meminfo";
            this.meminfo.ReadOnly = true;
            this.meminfo.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.meminfo.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.meminfo.Size = new System.Drawing.Size(593, 213);
            this.meminfo.TabIndex = 1;
            this.meminfo.WordWrap = false;
            this.meminfo.TextChanged += new System.EventHandler(this.meminfo_TextChanged);
            // 
            // pid
            // 
            this.pid.AutoSize = true;
            this.pid.Location = new System.Drawing.Point(21, 311);
            this.pid.Name = "pid";
            this.pid.Size = new System.Drawing.Size(31, 15);
            this.pid.TabIndex = 2;
            this.pid.Text = "PID";
            // 
            // inputPID
            // 
            this.inputPID.Location = new System.Drawing.Point(61, 308);
            this.inputPID.Name = "inputPID";
            this.inputPID.Size = new System.Drawing.Size(95, 25);
            this.inputPID.TabIndex = 3;
            this.inputPID.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // getmem
            // 
            this.getmem.Location = new System.Drawing.Point(165, 308);
            this.getmem.Name = "getmem";
            this.getmem.Size = new System.Drawing.Size(132, 25);
            this.getmem.TabIndex = 4;
            this.getmem.Text = "获取内存镜像";
            this.getmem.UseVisualStyleBackColor = true;
            this.getmem.Click += new System.EventHandler(this.getmem_Click);
            // 
            // phone_state
            // 
            this.phone_state.Location = new System.Drawing.Point(12, -1);
            this.phone_state.Multiline = true;
            this.phone_state.Name = "phone_state";
            this.phone_state.ReadOnly = true;
            this.phone_state.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.phone_state.Size = new System.Drawing.Size(472, 72);
            this.phone_state.TabIndex = 5;
            this.phone_state.TextChanged += new System.EventHandler(this.phone_state_TextChanged);
            // 
            // button_phone
            // 
            this.button_phone.CausesValidation = false;
            this.button_phone.Location = new System.Drawing.Point(499, 9);
            this.button_phone.Name = "button_phone";
            this.button_phone.Size = new System.Drawing.Size(106, 23);
            this.button_phone.TabIndex = 6;
            this.button_phone.Text = "手机状态";
            this.button_phone.UseVisualStyleBackColor = true;
            this.button_phone.Click += new System.EventHandler(this.button_phone_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // button_analysis
            // 
            this.button_analysis.Location = new System.Drawing.Point(398, 337);
            this.button_analysis.Name = "button_analysis";
            this.button_analysis.Size = new System.Drawing.Size(122, 25);
            this.button_analysis.TabIndex = 7;
            this.button_analysis.Text = "内存镜像分析";
            this.button_analysis.UseVisualStyleBackColor = true;
            this.button_analysis.Click += new System.EventHandler(this.button_analysis_Click);
            // 
            // result
            // 
            this.result.AcceptsReturn = true;
            this.result.AcceptsTab = true;
            this.result.CausesValidation = false;
            this.result.Location = new System.Drawing.Point(12, 409);
            this.result.Multiline = true;
            this.result.Name = "result";
            this.result.ReadOnly = true;
            this.result.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.result.Size = new System.Drawing.Size(590, 283);
            this.result.TabIndex = 8;
            // 
            // button_result
            // 
            this.button_result.CausesValidation = false;
            this.button_result.Location = new System.Drawing.Point(526, 339);
            this.button_result.Name = "button_result";
            this.button_result.Size = new System.Drawing.Size(93, 25);
            this.button_result.TabIndex = 9;
            this.button_result.Text = "显示结果";
            this.button_result.UseVisualStyleBackColor = true;
            this.button_result.Click += new System.EventHandler(this.button_result_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(21, 375);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(97, 15);
            this.label1.TabIndex = 10;
            this.label1.Text = "关键信息搜索";
            // 
            // keyword_search
            // 
            this.keyword_search.Location = new System.Drawing.Point(136, 372);
            this.keyword_search.Name = "keyword_search";
            this.keyword_search.Size = new System.Drawing.Size(276, 25);
            this.keyword_search.TabIndex = 11;
            // 
            // search
            // 
            this.search.Location = new System.Drawing.Point(436, 368);
            this.search.Name = "search";
            this.search.Size = new System.Drawing.Size(112, 28);
            this.search.TabIndex = 12;
            this.search.Text = "搜索";
            this.search.UseVisualStyleBackColor = true;
            this.search.Click += new System.EventHandler(this.button1_Click_1);
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Items.AddRange(new object[] {
            "网易邮箱",
            "陌陌",
            "微信(支付)"});
            this.comboBox1.Location = new System.Drawing.Point(165, 339);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(132, 23);
            this.comboBox1.TabIndex = 13;
            this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 339);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(150, 15);
            this.label2.TabIndex = 14;
            this.label2.Text = "内存镜像对应的应用";
            // 
            // saveFileDialog1
            // 
            this.saveFileDialog1.FileOk += new System.ComponentModel.CancelEventHandler(this.saveFileDialog1_FileOk);
            // 
            // button_savedir
            // 
            this.button_savedir.Location = new System.Drawing.Point(303, 337);
            this.button_savedir.Name = "button_savedir";
            this.button_savedir.Size = new System.Drawing.Size(89, 25);
            this.button_savedir.TabIndex = 15;
            this.button_savedir.Text = "保存路径";
            this.button_savedir.UseVisualStyleBackColor = true;
            this.button_savedir.Click += new System.EventHandler(this.button_savedir_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(617, 704);
            this.Controls.Add(this.button_savedir);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.search);
            this.Controls.Add(this.keyword_search);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button_result);
            this.Controls.Add(this.result);
            this.Controls.Add(this.button_analysis);
            this.Controls.Add(this.button_phone);
            this.Controls.Add(this.phone_state);
            this.Controls.Add(this.getmem);
            this.Controls.Add(this.inputPID);
            this.Controls.Add(this.pid);
            this.Controls.Add(this.meminfo);
            this.Controls.Add(this.dumpsys_meminfo);
            this.Name = "Form1";
            this.Text = "AndroidMemForensic";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button dumpsys_meminfo;
        private System.Windows.Forms.TextBox meminfo;
        private System.Windows.Forms.Label pid;
        private System.Windows.Forms.TextBox inputPID;
        private System.Windows.Forms.Button getmem;
        private System.Windows.Forms.TextBox phone_state;
        private System.Windows.Forms.Button button_phone;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button button_analysis;
        private System.Windows.Forms.TextBox result;
        private System.Windows.Forms.Button button_result;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox keyword_search;
        private System.Windows.Forms.Button search;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.Button button_savedir;
    }
}

