<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/examples/rag/">
      
      
        <link rel="prev" href="../flight-booking/">
      
      
        <link rel="next" href="../stream-markdown/">
      
      
      <link rel="icon" href="../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>RAG - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="RAG - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/examples/rag.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/examples/rag/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="RAG - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/examples/rag.png">
      
    
    
   <link href="../../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#rag" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="../.." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../img/logo-white.svg" alt="logo">

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"></path></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            PydanticAI
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              RAG
            
          </span>
        </div>
      </div>
    </div>
    
      
        <form class="md-header__option" data-md-component="palette">
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to light mode" type="radio" name="__palette" id="__palette_0">
    
      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_1">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7M9 21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1H9z"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to dark mode" type="radio" name="__palette" id="__palette_1">
    
      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_2" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7M9 21v-1h6v1a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1m3-17a5 5 0 0 0-5 5c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58a5 5 0 0 0-5-5"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="slate" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to system preference" type="radio" name="__palette" id="__palette_2">
    
      <label class="md-header__button md-icon" title="Switch to system preference" for="__palette_0" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 2c3.87 0 7 3.13 7 7 0 2.38-1.19 4.47-3 5.74V17c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-2.26C3.19 13.47 2 11.38 2 9c0-3.87 3.13-7 7-7M6 21v-1h6v1c0 .55-.45 1-1 1H7c-.55 0-1-.45-1-1M9 4C6.24 4 4 6.24 4 9c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58 0-2.76-2.24-5-5-5m10 9h-2l-3.2 9h1.9l.7-2h3.2l.7 2h1.9zm-2.15 5.65L18 15l1.15 3.65z"></path></svg>
      </label>
    
  
</form>
      
    
    
      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>
    
    
    
      <label class="md-header__button md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
      </label>
      <div class="md-search" role="dialog">
  <label class="md-search__overlay" for="__search"></label>
  <div class="md-search__inner" role="search">
    <form class="md-search__form" name="search">
      <input type="text" id="searchbox" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" required="">
      <label class="md-search__icon md-icon" for="__search">

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.516 6.516 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5Z"></path></svg>

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11h12Z"></path></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">

        <button id="searchbox-clear" type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">

          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41Z"></path></svg>
        </button>
      </nav>

        <div class="md-search__suggest"></div>

    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0">
        <div class="md-search-result">
          <div class="md-search-result__meta" id="type-to-start-searching">Type to start searching</div>
          <ol class="md-search-result__list" id="hits" role="presentation" hidden=""></ol>
        </div>
      </div>
    </div>
  </div>
</div>
    
    
      <div class="md-header__source">
        <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
      </div>
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation">
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    



<nav class="md-nav md-nav--primary" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href="../.." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../img/logo-white.svg" alt="logo">

    </a>
    PydanticAI
  </label>
  
    <div class="md-nav__source">
      <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
    </div>
  
  <ul class="md-nav__list">
    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../.." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../troubleshooting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Troubleshooting
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6">
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="">
            
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../mcp/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    MCP
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_6_14" id="__nav_6_14_label" tabindex="0">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_14_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6_14">
            <span class="md-nav__icon md-icon"></span>
            MCP
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../cli/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Command Line Interface (CLI)
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7" checked="">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#example-code" class="md-nav__link">
    <span class="md-ellipsis">
      Example Code
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/generation/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.generation
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" style="top: 48px;">
                <div class="md-sidebar__scrollwrap" style="height: 474px;">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#example-code" class="md-nav__link">
    <span class="md-ellipsis">
      Example Code
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="rag">RAG</h1>
<p>RAG search example. This demo allows you to ask question of the <a href="https://pydantic.dev/logfire">logfire</a> documentation.</p>
<p>Demonstrates:</p>
<ul>
<li><a href="../../tools/">tools</a></li>
<li><a href="../../dependencies/">agent dependencies</a></li>
<li>RAG search</li>
</ul>
<p>This is done by creating a database containing each section of the markdown documentation, then registering
the search tool with the PydanticAI agent.</p>
<p>Logic for extracting sections from markdown files and a JSON file with that data is available in
<a href="https://gist.github.com/samuelcolvin/4b5bb9bb163b1122ff17e29e48c10992">this gist</a>.</p>
<p><a href="https://github.com/pgvector/pgvector">PostgreSQL with pgvector</a> is used as the search database, the easiest way to download and run pgvector is using Docker:</p>
<div class="language-bash highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code>mkdir<span class="w"> </span>postgres-data
docker<span class="w"> </span>run<span class="w"> </span>--rm<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>-e<span class="w"> </span><span class="nv">POSTGRES_PASSWORD</span><span class="o">=</span>postgres<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>-p<span class="w"> </span><span class="m">54320</span>:5432<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>-v<span class="w"> </span><span class="sb">`</span><span class="nb">pwd</span><span class="sb">`</span>/postgres-data:/var/lib/postgresql/data<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>pgvector/pgvector:pg17
</code></pre></div>
<p>As with the <a href="../sql-gen/">SQL gen</a> example, we run postgres on port <code>54320</code> to avoid conflicts with any other postgres instances you may have running.
We also mount the PostgreSQL <code>data</code> directory locally to persist the data if you need to stop and restart the container.</p>
<p>With that running and <a href="../#usage">dependencies installed and environment variables set</a>, we can build the search database with (<strong>WARNING</strong>: this requires the <code>OPENAI_API_KEY</code> env variable and will calling the OpenAI embedding API around 300 times to generate embeddings for each section of the documentation):</p>
<div class="tabbed-set tabbed-alternate" data-tabs="1:2" style="--md-indicator-x: 0px; --md-indicator-width: 50px;"><input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio"><input id="__tabbed_1_2" name="__tabbed_1" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_1_1"><a href="#__tabbed_1_1" tabindex="-1">pip</a></label><label for="__tabbed_1_2"><a href="#__tabbed_1_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code>python<span class="w"> </span>-m<span class="w"> </span>pydantic_ai_examples.rag<span class="w"> </span>build
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code>uv<span class="w"> </span>run<span class="w"> </span>-m<span class="w"> </span>pydantic_ai_examples.rag<span class="w"> </span>build
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<p>(Note building the database doesn't use PydanticAI right now, instead it uses the OpenAI SDK directly.)</p>
<p>You can then ask the agent a question with:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="2:2" style="--md-indicator-x: 0px; --md-indicator-width: 50px;"><input checked="checked" id="__tabbed_2_1" name="__tabbed_2" type="radio"><input id="__tabbed_2_2" name="__tabbed_2" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_2_1"><a href="#__tabbed_2_1" tabindex="-1">pip</a></label><label for="__tabbed_2_2"><a href="#__tabbed_2_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code>python<span class="w"> </span>-m<span class="w"> </span>pydantic_ai_examples.rag<span class="w"> </span>search<span class="w"> </span><span class="s2">"How do I configure logfire to work with FastAPI?"</span>
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code>uv<span class="w"> </span>run<span class="w"> </span>-m<span class="w"> </span>pydantic_ai_examples.rag<span class="w"> </span>search<span class="w"> </span><span class="s2">"How do I configure logfire to work with FastAPI?"</span>
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<h2 id="example-code">Example Code</h2>
<div class="language-python highlight"><span class="filename">rag.py</span><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">__future__</span><span class="w"> </span><span class="kn">import</span> <span class="n">annotations</span> <span class="k">as</span> <span class="n">_annotations</span>

<span class="kn">import</span><span class="w"> </span><span class="nn">asyncio</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">re</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">sys</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">unicodedata</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">contextlib</span><span class="w"> </span><span class="kn">import</span> <span class="n">asynccontextmanager</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">dataclasses</span><span class="w"> </span><span class="kn">import</span> <span class="n">dataclass</span>

<span class="kn">import</span><span class="w"> </span><span class="nn">asyncpg</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">httpx</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">logfire</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">pydantic_core</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncOpenAI</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">TypeAdapter</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">typing_extensions</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncGenerator</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunContext</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.agent</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="c1"># 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured</span>
<span class="n">logfire</span><span class="o">.</span><span class="n">configure</span><span class="p">(</span><span class="n">send_to_logfire</span><span class="o">=</span><span class="s1">'if-token-present'</span><span class="p">)</span>
<span class="n">logfire</span><span class="o">.</span><span class="n">instrument_asyncpg</span><span class="p">()</span>


<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Deps</span><span class="p">:</span>
    <span class="n">openai</span><span class="p">:</span> <span class="n">AsyncOpenAI</span>
    <span class="n">pool</span><span class="p">:</span> <span class="n">asyncpg</span><span class="o">.</span><span class="n">Pool</span>


<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">,</span> <span class="n">deps_type</span><span class="o">=</span><span class="n">Deps</span><span class="p">,</span> <span class="n">instrument</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>


<span class="nd">@agent</span><span class="o">.</span><span class="n">tool</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">retrieve</span><span class="p">(</span><span class="n">context</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">Deps</span><span class="p">],</span> <span class="n">search_query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Retrieve documentation sections based on a search query.</span>

<span class="sd">    Args:</span>
<span class="sd">        context: The call context.</span>
<span class="sd">        search_query: The search query.</span>
<span class="sd">    """</span>
    <span class="k">with</span> <span class="n">logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span>
        <span class="s1">'create embedding for {search_query=}'</span><span class="p">,</span> <span class="n">search_query</span><span class="o">=</span><span class="n">search_query</span>
    <span class="p">):</span>
        <span class="n">embedding</span> <span class="o">=</span> <span class="k">await</span> <span class="n">context</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">openai</span><span class="o">.</span><span class="n">embeddings</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
            <span class="nb">input</span><span class="o">=</span><span class="n">search_query</span><span class="p">,</span>
            <span class="n">model</span><span class="o">=</span><span class="s1">'text-embedding-3-small'</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">embedding</span><span class="o">.</span><span class="n">data</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">,</span> <span class="p">(</span>
        <span class="sa">f</span><span class="s1">'Expected 1 embedding, got </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">embedding</span><span class="o">.</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">, doc query: </span><span class="si">{</span><span class="n">search_query</span><span class="si">!r}</span><span class="s1">'</span>
    <span class="p">)</span>
    <span class="n">embedding</span> <span class="o">=</span> <span class="n">embedding</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">embedding</span>
    <span class="n">embedding_json</span> <span class="o">=</span> <span class="n">pydantic_core</span><span class="o">.</span><span class="n">to_json</span><span class="p">(</span><span class="n">embedding</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>
    <span class="n">rows</span> <span class="o">=</span> <span class="k">await</span> <span class="n">context</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">pool</span><span class="o">.</span><span class="n">fetch</span><span class="p">(</span>
        <span class="s1">'SELECT url, title, content FROM doc_sections ORDER BY embedding &lt;-&gt; $1 LIMIT 8'</span><span class="p">,</span>
        <span class="n">embedding_json</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="s1">'</span><span class="se">\n\n</span><span class="s1">'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
        <span class="sa">f</span><span class="s1">'# </span><span class="si">{</span><span class="n">row</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span><span class="si">}</span><span class="se">\n</span><span class="s1">Documentation URL:</span><span class="si">{</span><span class="n">row</span><span class="p">[</span><span class="s2">"url"</span><span class="p">]</span><span class="si">}</span><span class="se">\n\n</span><span class="si">{</span><span class="n">row</span><span class="p">[</span><span class="s2">"content"</span><span class="p">]</span><span class="si">}</span><span class="se">\n</span><span class="s1">'</span>
        <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">rows</span>
    <span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run_agent</span><span class="p">(</span><span class="n">question</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Entry point to run the agent and perform RAG based question answering."""</span>
    <span class="n">openai</span> <span class="o">=</span> <span class="n">AsyncOpenAI</span><span class="p">()</span>
    <span class="n">logfire</span><span class="o">.</span><span class="n">instrument_openai</span><span class="p">(</span><span class="n">openai</span><span class="p">)</span>

    <span class="n">logfire</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s1">'Asking "</span><span class="si">{question}</span><span class="s1">"'</span><span class="p">,</span> <span class="n">question</span><span class="o">=</span><span class="n">question</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">with</span> <span class="n">database_connect</span><span class="p">(</span><span class="kc">False</span><span class="p">)</span> <span class="k">as</span> <span class="n">pool</span><span class="p">:</span>
        <span class="n">deps</span> <span class="o">=</span> <span class="n">Deps</span><span class="p">(</span><span class="n">openai</span><span class="o">=</span><span class="n">openai</span><span class="p">,</span> <span class="n">pool</span><span class="o">=</span><span class="n">pool</span><span class="p">)</span>
        <span class="n">answer</span> <span class="o">=</span> <span class="k">await</span> <span class="n">agent</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">question</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">answer</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>


<span class="c1">#######################################################</span>
<span class="c1"># The rest of this file is dedicated to preparing the #</span>
<span class="c1"># search database, and some utilities.                #</span>
<span class="c1">#######################################################</span>

<span class="c1"># JSON document from</span>
<span class="c1"># https://gist.github.com/samuelcolvin/4b5bb9bb163b1122ff17e29e48c10992</span>
<span class="n">DOCS_JSON</span> <span class="o">=</span> <span class="p">(</span>
    <span class="s1">'https://gist.githubusercontent.com/'</span>
    <span class="s1">'samuelcolvin/4b5bb9bb163b1122ff17e29e48c10992/raw/'</span>
    <span class="s1">'80c5925c42f1442c24963aaf5eb1a324d47afe95/logfire_docs.json'</span>
<span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">build_search_db</span><span class="p">():</span>
<span class="w">    </span><span class="sd">"""Build the search database."""</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span><span class="p">()</span> <span class="k">as</span> <span class="n">client</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">client</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">DOCS_JSON</span><span class="p">)</span>
        <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
    <span class="n">sections</span> <span class="o">=</span> <span class="n">sessions_ta</span><span class="o">.</span><span class="n">validate_json</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>

    <span class="n">openai</span> <span class="o">=</span> <span class="n">AsyncOpenAI</span><span class="p">()</span>
    <span class="n">logfire</span><span class="o">.</span><span class="n">instrument_openai</span><span class="p">(</span><span class="n">openai</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">with</span> <span class="n">database_connect</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">pool</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'create schema'</span><span class="p">):</span>
            <span class="k">async</span> <span class="k">with</span> <span class="n">pool</span><span class="o">.</span><span class="n">acquire</span><span class="p">()</span> <span class="k">as</span> <span class="n">conn</span><span class="p">:</span>
                <span class="k">async</span> <span class="k">with</span> <span class="n">conn</span><span class="o">.</span><span class="n">transaction</span><span class="p">():</span>
                    <span class="k">await</span> <span class="n">conn</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">DB_SCHEMA</span><span class="p">)</span>

        <span class="n">sem</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Semaphore</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
        <span class="k">async</span> <span class="k">with</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">TaskGroup</span><span class="p">()</span> <span class="k">as</span> <span class="n">tg</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">section</span> <span class="ow">in</span> <span class="n">sections</span><span class="p">:</span>
                <span class="n">tg</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">insert_doc_section</span><span class="p">(</span><span class="n">sem</span><span class="p">,</span> <span class="n">openai</span><span class="p">,</span> <span class="n">pool</span><span class="p">,</span> <span class="n">section</span><span class="p">))</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">insert_doc_section</span><span class="p">(</span>
    <span class="n">sem</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Semaphore</span><span class="p">,</span>
    <span class="n">openai</span><span class="p">:</span> <span class="n">AsyncOpenAI</span><span class="p">,</span>
    <span class="n">pool</span><span class="p">:</span> <span class="n">asyncpg</span><span class="o">.</span><span class="n">Pool</span><span class="p">,</span>
    <span class="n">section</span><span class="p">:</span> <span class="n">DocsSection</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">sem</span><span class="p">:</span>
        <span class="n">url</span> <span class="o">=</span> <span class="n">section</span><span class="o">.</span><span class="n">url</span><span class="p">()</span>
        <span class="n">exists</span> <span class="o">=</span> <span class="k">await</span> <span class="n">pool</span><span class="o">.</span><span class="n">fetchval</span><span class="p">(</span><span class="s1">'SELECT 1 FROM doc_sections WHERE url = $1'</span><span class="p">,</span> <span class="n">url</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">exists</span><span class="p">:</span>
            <span class="n">logfire</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s1">'Skipping {url=}'</span><span class="p">,</span> <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">)</span>
            <span class="k">return</span>

        <span class="k">with</span> <span class="n">logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'create embedding for {url=}'</span><span class="p">,</span> <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">):</span>
            <span class="n">embedding</span> <span class="o">=</span> <span class="k">await</span> <span class="n">openai</span><span class="o">.</span><span class="n">embeddings</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
                <span class="nb">input</span><span class="o">=</span><span class="n">section</span><span class="o">.</span><span class="n">embedding_content</span><span class="p">(),</span>
                <span class="n">model</span><span class="o">=</span><span class="s1">'text-embedding-3-small'</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">embedding</span><span class="o">.</span><span class="n">data</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">,</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s1">'Expected 1 embedding, got </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">embedding</span><span class="o">.</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">, doc section: </span><span class="si">{</span><span class="n">section</span><span class="si">}</span><span class="s1">'</span>
        <span class="p">)</span>
        <span class="n">embedding</span> <span class="o">=</span> <span class="n">embedding</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">embedding</span>
        <span class="n">embedding_json</span> <span class="o">=</span> <span class="n">pydantic_core</span><span class="o">.</span><span class="n">to_json</span><span class="p">(</span><span class="n">embedding</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>
        <span class="k">await</span> <span class="n">pool</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
            <span class="s1">'INSERT INTO doc_sections (url, title, content, embedding) VALUES ($1, $2, $3, $4)'</span><span class="p">,</span>
            <span class="n">url</span><span class="p">,</span>
            <span class="n">section</span><span class="o">.</span><span class="n">title</span><span class="p">,</span>
            <span class="n">section</span><span class="o">.</span><span class="n">content</span><span class="p">,</span>
            <span class="n">embedding_json</span><span class="p">,</span>
        <span class="p">)</span>


<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">DocsSection</span><span class="p">:</span>
    <span class="nb">id</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">parent</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">path</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">level</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">title</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">content</span><span class="p">:</span> <span class="nb">str</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">url_path</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s1">'\.md$'</span><span class="p">,</span> <span class="s1">''</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s1">'https://logfire.pydantic.dev/docs/</span><span class="si">{</span><span class="n">url_path</span><span class="si">}</span><span class="s1">/#</span><span class="si">{</span><span class="n">slugify</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">title</span><span class="p">,</span><span class="w"> </span><span class="s2">"-"</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">embedding_content</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s1">'</span><span class="se">\n\n</span><span class="s1">'</span><span class="o">.</span><span class="n">join</span><span class="p">((</span><span class="sa">f</span><span class="s1">'path: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span> <span class="sa">f</span><span class="s1">'title: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">title</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">))</span>


<span class="n">sessions_ta</span> <span class="o">=</span> <span class="n">TypeAdapter</span><span class="p">(</span><span class="nb">list</span><span class="p">[</span><span class="n">DocsSection</span><span class="p">])</span>


<span class="c1"># pyright: reportUnknownMemberType=false</span>
<span class="c1"># pyright: reportUnknownVariableType=false</span>
<span class="nd">@asynccontextmanager</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">database_connect</span><span class="p">(</span>
    <span class="n">create_db</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncGenerator</span><span class="p">[</span><span class="n">asyncpg</span><span class="o">.</span><span class="n">Pool</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
    <span class="n">server_dsn</span><span class="p">,</span> <span class="n">database</span> <span class="o">=</span> <span class="p">(</span>
        <span class="s1">'postgresql://postgres:postgres@localhost:54320'</span><span class="p">,</span>
        <span class="s1">'pydantic_ai_rag'</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="n">create_db</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'check and create DB'</span><span class="p">):</span>
            <span class="n">conn</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncpg</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">server_dsn</span><span class="p">)</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">db_exists</span> <span class="o">=</span> <span class="k">await</span> <span class="n">conn</span><span class="o">.</span><span class="n">fetchval</span><span class="p">(</span>
                    <span class="s1">'SELECT 1 FROM pg_database WHERE datname = $1'</span><span class="p">,</span> <span class="n">database</span>
                <span class="p">)</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">db_exists</span><span class="p">:</span>
                    <span class="k">await</span> <span class="n">conn</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="sa">f</span><span class="s1">'CREATE DATABASE </span><span class="si">{</span><span class="n">database</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
            <span class="k">finally</span><span class="p">:</span>
                <span class="k">await</span> <span class="n">conn</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>

    <span class="n">pool</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncpg</span><span class="o">.</span><span class="n">create_pool</span><span class="p">(</span><span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">server_dsn</span><span class="si">}</span><span class="s1">/</span><span class="si">{</span><span class="n">database</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">yield</span> <span class="n">pool</span>
    <span class="k">finally</span><span class="p">:</span>
        <span class="k">await</span> <span class="n">pool</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>


<span class="n">DB_SCHEMA</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">CREATE EXTENSION IF NOT EXISTS vector;</span>

<span class="s2">CREATE TABLE IF NOT EXISTS doc_sections (</span>
<span class="s2">    id serial PRIMARY KEY,</span>
<span class="s2">    url text NOT NULL UNIQUE,</span>
<span class="s2">    title text NOT NULL,</span>
<span class="s2">    content text NOT NULL,</span>
<span class="s2">    -- text-embedding-3-small returns a vector of 1536 floats</span>
<span class="s2">    embedding vector(1536) NOT NULL</span>
<span class="s2">);</span>
<span class="s2">CREATE INDEX IF NOT EXISTS idx_doc_sections_embedding ON doc_sections USING hnsw (embedding vector_l2_ops);</span>
<span class="s2">"""</span>


<span class="k">def</span><span class="w"> </span><span class="nf">slugify</span><span class="p">(</span><span class="n">value</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">unicode</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Slugify a string, to make it URL friendly."""</span>
    <span class="c1"># Taken unchanged from https://github.com/Python-Markdown/markdown/blob/3.7/markdown/extensions/toc.py#L38</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">unicode</span><span class="p">:</span>
        <span class="c1"># Replace Extended Latin characters with ASCII, i.e. `žlutý` =&gt; `zluty`</span>
        <span class="n">value</span> <span class="o">=</span> <span class="n">unicodedata</span><span class="o">.</span><span class="n">normalize</span><span class="p">(</span><span class="s1">'NFKD'</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
        <span class="n">value</span> <span class="o">=</span> <span class="n">value</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s1">'ascii'</span><span class="p">,</span> <span class="s1">'ignore'</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s1">'ascii'</span><span class="p">)</span>
    <span class="n">value</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s1">'[^\w\s-]'</span><span class="p">,</span> <span class="s1">''</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">rf</span><span class="s1">'[</span><span class="si">{</span><span class="n">separator</span><span class="si">}</span><span class="s1">\s]+'</span><span class="p">,</span> <span class="n">separator</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>


<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s1">'__main__'</span><span class="p">:</span>
    <span class="n">action</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="k">else</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">action</span> <span class="o">==</span> <span class="s1">'build'</span><span class="p">:</span>
        <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">build_search_db</span><span class="p">())</span>
    <span class="k">elif</span> <span class="n">action</span> <span class="o">==</span> <span class="s1">'search'</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span> <span class="o">==</span> <span class="mi">3</span><span class="p">:</span>
            <span class="n">q</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">q</span> <span class="o">=</span> <span class="s1">'How do I configure logfire to work with FastAPI?'</span>
        <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">run_agent</span><span class="p">(</span><span class="n">q</span><span class="p">))</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span>
            <span class="s1">'uv run --extra examples -m pydantic_ai_examples.rag build|search'</span><span class="p">,</span>
            <span class="n">file</span><span class="o">=</span><span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</code></pre></div>







  
  






                
              </article>
            </div>
          
          
  <script>var tabs=__md_get("__tabs");if(Array.isArray(tabs))e:for(var set of document.querySelectorAll(".tabbed-set")){var labels=set.querySelector(".tabbed-labels");for(var tab of tabs)for(var label of labels.getElementsByTagName("label"))if(label.innerText.trim()===tab){var input=document.getElementById(label.htmlFor);input.checked=!0;continue e}}</script>

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
      </main>
      
        <footer class="md-footer">
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
    <div class="md-copyright__highlight">
      © Pydantic Services Inc. 2024 to present
    </div>
  
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
    
    <script id="__config" type="application/json">{"base": "../..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>