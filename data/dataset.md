<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/pydantic_evals/dataset/">
      
      
        <link rel="prev" href="../../pydantic_graph/exceptions/">
      
      
        <link rel="next" href="../evaluators/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_evals.dataset - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_evals.dataset - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_evals/dataset.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/pydantic_evals/dataset/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_evals.dataset - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_evals/dataset.png">
      
    
    
   <link href="../../../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../../../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#pydantic_evalsdataset" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="../../.." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

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
            
              pydantic_evals.dataset
            
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
    <a href="../../.." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

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
      <a href="../../.." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../troubleshooting/" class="md-nav__link">
        
  
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
      <a href="../../../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../../mcp/" class="md-nav__link ">
              
  
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
      <a href="../../../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../cli/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Command Line Interface (CLI)
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../../examples/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8" checked="">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.dataset" class="md-nav__link">
    <span class="md-ellipsis">
      dataset
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case" class="md-nav__link">
    <span class="md-ellipsis">
      Case
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Case">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.inputs" class="md-nav__link">
    <span class="md-ellipsis">
      inputs
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.metadata" class="md-nav__link">
    <span class="md-ellipsis">
      metadata
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.expected_output" class="md-nav__link">
    <span class="md-ellipsis">
      expected_output
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.evaluators" class="md-nav__link">
    <span class="md-ellipsis">
      evaluators
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset" class="md-nav__link">
    <span class="md-ellipsis">
      Dataset
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Dataset">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.cases" class="md-nav__link">
    <span class="md-ellipsis">
      cases
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.evaluators" class="md-nav__link">
    <span class="md-ellipsis">
      evaluators
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.evaluate" class="md-nav__link">
    <span class="md-ellipsis">
      evaluate
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.evaluate_sync" class="md-nav__link">
    <span class="md-ellipsis">
      evaluate_sync
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.add_case" class="md-nav__link">
    <span class="md-ellipsis">
      add_case
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.add_evaluator" class="md-nav__link">
    <span class="md-ellipsis">
      add_evaluator
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.from_file" class="md-nav__link">
    <span class="md-ellipsis">
      from_file
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.from_text" class="md-nav__link">
    <span class="md-ellipsis">
      from_text
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.from_dict" class="md-nav__link">
    <span class="md-ellipsis">
      from_dict
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.to_file" class="md-nav__link">
    <span class="md-ellipsis">
      to_file
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.model_json_schema_with_evaluators" class="md-nav__link">
    <span class="md-ellipsis">
      model_json_schema_with_evaluators
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.set_eval_attribute" class="md-nav__link">
    <span class="md-ellipsis">
      set_eval_attribute
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.increment_eval_metric" class="md-nav__link">
    <span class="md-ellipsis">
      increment_eval_metric
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../generation/" class="md-nav__link">
        
  
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
  <a href="#pydantic_evals.dataset" class="md-nav__link">
    <span class="md-ellipsis">
      dataset
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case" class="md-nav__link">
    <span class="md-ellipsis">
      Case
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Case">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.inputs" class="md-nav__link">
    <span class="md-ellipsis">
      inputs
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.metadata" class="md-nav__link">
    <span class="md-ellipsis">
      metadata
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.expected_output" class="md-nav__link">
    <span class="md-ellipsis">
      expected_output
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Case.evaluators" class="md-nav__link">
    <span class="md-ellipsis">
      evaluators
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset" class="md-nav__link">
    <span class="md-ellipsis">
      Dataset
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Dataset">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.cases" class="md-nav__link">
    <span class="md-ellipsis">
      cases
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.evaluators" class="md-nav__link">
    <span class="md-ellipsis">
      evaluators
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.evaluate" class="md-nav__link">
    <span class="md-ellipsis">
      evaluate
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.evaluate_sync" class="md-nav__link">
    <span class="md-ellipsis">
      evaluate_sync
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.add_case" class="md-nav__link">
    <span class="md-ellipsis">
      add_case
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.add_evaluator" class="md-nav__link">
    <span class="md-ellipsis">
      add_evaluator
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.from_file" class="md-nav__link">
    <span class="md-ellipsis">
      from_file
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.from_text" class="md-nav__link">
    <span class="md-ellipsis">
      from_text
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.from_dict" class="md-nav__link">
    <span class="md-ellipsis">
      from_dict
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.to_file" class="md-nav__link">
    <span class="md-ellipsis">
      to_file
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.Dataset.model_json_schema_with_evaluators" class="md-nav__link">
    <span class="md-ellipsis">
      model_json_schema_with_evaluators
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.set_eval_attribute" class="md-nav__link">
    <span class="md-ellipsis">
      set_eval_attribute
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.dataset.increment_eval_metric" class="md-nav__link">
    <span class="md-ellipsis">
      increment_eval_metric
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
                
                  


  
  


<h1 id="pydantic_evalsdataset"><code>pydantic_evals.dataset</code></h1>


<div class="doc doc-object doc-module">



<a id="pydantic_evals.dataset"></a>
    <div class="doc doc-contents first">

        <p>Dataset management for pydantic evals.</p>
<p>This module provides functionality for creating, loading, saving, and evaluating datasets of test cases.
Each case must have inputs, and can optionally have a name, expected output, metadata, and case-specific evaluators.</p>
<p>Datasets can be loaded from and saved to YAML or JSON files, and can be evaluated against
a task function to produce an evaluation report.</p>








  <div class="doc doc-children">















































































<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.dataset.Case" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">Case</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>]</code></p>


        <p>A single row of a <a class="autorefs autorefs-internal" href="#pydantic_evals.dataset.Dataset"><code>Dataset</code></a>.</p>
<p>Each case represents a single test scenario with inputs to test. A case may optionally specify a name, expected
outputs to compare against, and arbitrary metadata.</p>
<p>Cases can also have their own specific evaluators which are run in addition to dataset-level evaluators.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals</span><span class="w"> </span><span class="kn">import</span> <span class="n">Case</span>

<span class="n">case</span> <span class="o">=</span> <span class="n">Case</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s1">'Simple addition'</span><span class="p">,</span>
    <span class="n">inputs</span><span class="o">=</span><span class="p">{</span><span class="s1">'a'</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s1">'b'</span><span class="p">:</span> <span class="mi">2</span><span class="p">},</span>
    <span class="n">expected_output</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s1">'description'</span><span class="p">:</span> <span class="s1">'Tests basic addition'</span><span class="p">},</span>
<span class="p">)</span>
</code></pre></div><p></p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span></pre></div></td><td class="code"><div><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code tabindex="0"><span class="nd">@dataclass</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Case</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""A single row of a [`Dataset`][pydantic_evals.Dataset].</span>

<span class="sd">    Each case represents a single test scenario with inputs to test. A case may optionally specify a name, expected</span>
<span class="sd">    outputs to compare against, and arbitrary metadata.</span>

<span class="sd">    Cases can also have their own specific evaluators which are run in addition to dataset-level evaluators.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from pydantic_evals import Case</span>

<span class="sd">    case = Case(</span>
<span class="sd">        name='Simple addition',</span>
<span class="sd">        inputs={'a': 1, 'b': 2},</span>
<span class="sd">        expected_output=3,</span>
<span class="sd">        metadata={'description': 'Tests basic addition'},</span>
<span class="sd">    )</span>
<span class="sd">    ```</span>
<span class="sd">    """</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Name of the case. This is used to identify the case in the report and can be used to filter cases."""</span>
    <span class="n">inputs</span><span class="p">:</span> <span class="n">InputsT</span>
<span class="w">    </span><span class="sd">"""Inputs to the task. This is the input to the task that will be evaluated."""</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">MetadataT</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Metadata to be used in the evaluation.</span>

<span class="sd">    This can be used to provide additional information about the case to the evaluators.</span>
<span class="sd">    """</span>
    <span class="n">expected_output</span><span class="p">:</span> <span class="n">OutputT</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Expected output of the task. This is the expected output of the task that will be evaluated."""</span>
    <span class="n">evaluators</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""Evaluators to be used just on this case."""</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">inputs</span><span class="p">:</span> <span class="n">InputsT</span><span class="p">,</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">MetadataT</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">expected_output</span><span class="p">:</span> <span class="n">OutputT</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">evaluators</span><span class="p">:</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">],</span> <span class="o">...</span><span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize a new test case.</span>

<span class="sd">        Args:</span>
<span class="sd">            name: Optional name for the case. If not provided, a generic name will be assigned when added to a dataset.</span>
<span class="sd">            inputs: The inputs to the task being evaluated.</span>
<span class="sd">            metadata: Optional metadata for the case, which can be used by evaluators.</span>
<span class="sd">            expected_output: Optional expected output of the task, used for comparison in evaluators.</span>
<span class="sd">            evaluators: Tuple of evaluators specific to this case. These are in addition to any</span>
<span class="sd">                dataset-level evaluators.</span>

<span class="sd">        """</span>
        <span class="c1"># Note: `evaluators` must be a tuple instead of Sequence due to misbehavior with pyright's generic parameter</span>
        <span class="c1"># inference if it has type `Sequence`</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">inputs</span> <span class="o">=</span> <span class="n">inputs</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">expected_output</span> <span class="o">=</span> <span class="n">expected_output</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">evaluators</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.dataset.Case.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">inputs</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">expected_output</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">evaluators</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple">tuple</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">],</span> <span class="o">...</span>
    <span class="p">]</span> <span class="o">=</span> <span class="p">()</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Initialize a new test case.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional name for the case. If not provided, a generic name will be assigned when added to a dataset.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>inputs</code>
            </td>
            <td>
                  <code><span title="pydantic_evals.dataset.InputsT">InputsT</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The inputs to the task being evaluated.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>metadata</code>
            </td>
            <td>
                  <code><span title="pydantic_evals.dataset.MetadataT">MetadataT</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional metadata for the case, which can be used by evaluators.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>expected_output</code>
            </td>
            <td>
                  <code><span title="pydantic_evals.dataset.OutputT">OutputT</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional expected output of the task, used for comparison in evaluators.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>evaluators</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple">tuple</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>], ...]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Tuple of evaluators specific to this case. These are in addition to any
dataset-level evaluators.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span></pre></div></td><td class="code"><div><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">inputs</span><span class="p">:</span> <span class="n">InputsT</span><span class="p">,</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">MetadataT</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">expected_output</span><span class="p">:</span> <span class="n">OutputT</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">evaluators</span><span class="p">:</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">],</span> <span class="o">...</span><span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Initialize a new test case.</span>

<span class="sd">    Args:</span>
<span class="sd">        name: Optional name for the case. If not provided, a generic name will be assigned when added to a dataset.</span>
<span class="sd">        inputs: The inputs to the task being evaluated.</span>
<span class="sd">        metadata: Optional metadata for the case, which can be used by evaluators.</span>
<span class="sd">        expected_output: Optional expected output of the task, used for comparison in evaluators.</span>
<span class="sd">        evaluators: Tuple of evaluators specific to this case. These are in addition to any</span>
<span class="sd">            dataset-level evaluators.</span>

<span class="sd">    """</span>
    <span class="c1"># Note: `evaluators` must be a tuple instead of Sequence due to misbehavior with pyright's generic parameter</span>
    <span class="c1"># inference if it has type `Sequence`</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">inputs</span> <span class="o">=</span> <span class="n">inputs</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">expected_output</span> <span class="o">=</span> <span class="n">expected_output</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">evaluators</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.dataset.Case.name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n"><span title="pydantic_evals.dataset.Case(name)">name</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Name of the case. This is used to identify the case in the report and can be used to filter cases.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.dataset.Case.inputs" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">inputs</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="n">inputs</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span> <span class="o">=</span> <span class="n"><span title="pydantic_evals.dataset.Case(inputs)">inputs</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Inputs to the task. This is the input to the task that will be evaluated.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.dataset.Case.metadata" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">metadata</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="n">metadata</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n"><span title="pydantic_evals.dataset.Case(metadata)">metadata</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Metadata to be used in the evaluation.</p>
<p>This can be used to provide additional information about the case to the evaluators.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.dataset.Case.expected_output" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">expected_output</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="n">expected_output</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n"><span title="pydantic_evals.dataset.Case(expected_output)">expected_output</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Expected output of the task. This is the expected output of the task that will be evaluated.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.dataset.Case.evaluators" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">evaluators</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="n">evaluators</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">]]</span> <span class="o">=</span> <span class="p">(</span>
    <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">(</span><span class="n"><span title="pydantic_evals.dataset.Case(evaluators)">evaluators</span></span><span class="p">)</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Evaluators to be used just on this case.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.dataset.Dataset" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">Dataset</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="pydantic.BaseModel" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel">BaseModel</a></code>, <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>]</code></p>


        <p>A dataset of test <a class="autorefs autorefs-internal" href="#pydantic_evals.dataset.Case">cases</a>.</p>
<p>Datasets allow you to organize a collection of test cases and evaluate them against a task function.
They can be loaded from and saved to YAML or JSON files, and can have dataset-level evaluators that
apply to all cases.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code><span class="c1"># Create a dataset with two test cases</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">dataclasses</span><span class="w"> </span><span class="kn">import</span> <span class="n">dataclass</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals</span><span class="w"> </span><span class="kn">import</span> <span class="n">Case</span><span class="p">,</span> <span class="n">Dataset</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.evaluators</span><span class="w"> </span><span class="kn">import</span> <span class="n">Evaluator</span><span class="p">,</span> <span class="n">EvaluatorContext</span>


<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">ExactMatch</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">):</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span> <span class="o">==</span> <span class="n">ctx</span><span class="o">.</span><span class="n">expected_output</span>

<span class="n">dataset</span> <span class="o">=</span> <span class="n">Dataset</span><span class="p">(</span>
    <span class="n">cases</span><span class="o">=</span><span class="p">[</span>
        <span class="n">Case</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s1">'test1'</span><span class="p">,</span> <span class="n">inputs</span><span class="o">=</span><span class="p">{</span><span class="s1">'text'</span><span class="p">:</span> <span class="s1">'Hello'</span><span class="p">},</span> <span class="n">expected_output</span><span class="o">=</span><span class="s1">'HELLO'</span><span class="p">),</span>
        <span class="n">Case</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s1">'test2'</span><span class="p">,</span> <span class="n">inputs</span><span class="o">=</span><span class="p">{</span><span class="s1">'text'</span><span class="p">:</span> <span class="s1">'World'</span><span class="p">},</span> <span class="n">expected_output</span><span class="o">=</span><span class="s1">'WORLD'</span><span class="p">),</span>
    <span class="p">],</span>
    <span class="n">evaluators</span><span class="o">=</span><span class="p">[</span><span class="n">ExactMatch</span><span class="p">()],</span>
<span class="p">)</span>

<span class="c1"># Evaluate the dataset against a task function</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">uppercase</span><span class="p">(</span><span class="n">inputs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">return</span> <span class="n">inputs</span><span class="p">[</span><span class="s1">'text'</span><span class="p">]</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">report</span> <span class="o">=</span> <span class="k">await</span> <span class="n">dataset</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">uppercase</span><span class="p">)</span>
    <span class="n">report</span><span class="o">.</span><span class="n">print</span><span class="p">()</span>
<span class="sd">'''</span>
<span class="sd">   Evaluation Summary: uppercase</span>
<span class="sd">┏━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓</span>
<span class="sd">┃ Case ID  ┃ Assertions ┃ Duration ┃</span>
<span class="sd">┡━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩</span>
<span class="sd">│ test1    │ ✔          │     10ms │</span>
<span class="sd">├──────────┼────────────┼──────────┤</span>
<span class="sd">│ test2    │ ✔          │     10ms │</span>
<span class="sd">├──────────┼────────────┼──────────┤</span>
<span class="sd">│ Averages │ 100.0% ✔   │     10ms │</span>
<span class="sd">└──────────┴────────────┴──────────┘</span>
<span class="sd">'''</span>
</code></pre></div><p></p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span>
<span class="normal">612</span>
<span class="normal">613</span>
<span class="normal">614</span>
<span class="normal">615</span>
<span class="normal">616</span>
<span class="normal">617</span>
<span class="normal">618</span>
<span class="normal">619</span>
<span class="normal">620</span>
<span class="normal">621</span>
<span class="normal">622</span>
<span class="normal">623</span>
<span class="normal">624</span>
<span class="normal">625</span>
<span class="normal">626</span>
<span class="normal">627</span>
<span class="normal">628</span>
<span class="normal">629</span>
<span class="normal">630</span>
<span class="normal">631</span>
<span class="normal">632</span>
<span class="normal">633</span>
<span class="normal">634</span>
<span class="normal">635</span>
<span class="normal">636</span>
<span class="normal">637</span>
<span class="normal">638</span>
<span class="normal">639</span>
<span class="normal">640</span>
<span class="normal">641</span>
<span class="normal">642</span>
<span class="normal">643</span>
<span class="normal">644</span>
<span class="normal">645</span>
<span class="normal">646</span>
<span class="normal">647</span>
<span class="normal">648</span>
<span class="normal">649</span>
<span class="normal">650</span>
<span class="normal">651</span>
<span class="normal">652</span>
<span class="normal">653</span>
<span class="normal">654</span>
<span class="normal">655</span>
<span class="normal">656</span>
<span class="normal">657</span>
<span class="normal">658</span>
<span class="normal">659</span>
<span class="normal">660</span>
<span class="normal">661</span>
<span class="normal">662</span>
<span class="normal">663</span>
<span class="normal">664</span>
<span class="normal">665</span>
<span class="normal">666</span>
<span class="normal">667</span>
<span class="normal">668</span>
<span class="normal">669</span>
<span class="normal">670</span>
<span class="normal">671</span>
<span class="normal">672</span>
<span class="normal">673</span>
<span class="normal">674</span>
<span class="normal">675</span>
<span class="normal">676</span>
<span class="normal">677</span>
<span class="normal">678</span>
<span class="normal">679</span>
<span class="normal">680</span>
<span class="normal">681</span>
<span class="normal">682</span>
<span class="normal">683</span>
<span class="normal">684</span>
<span class="normal">685</span>
<span class="normal">686</span>
<span class="normal">687</span>
<span class="normal">688</span>
<span class="normal">689</span>
<span class="normal">690</span>
<span class="normal">691</span>
<span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span>
<span class="normal">699</span>
<span class="normal">700</span>
<span class="normal">701</span>
<span class="normal">702</span>
<span class="normal">703</span>
<span class="normal">704</span>
<span class="normal">705</span>
<span class="normal">706</span>
<span class="normal">707</span>
<span class="normal">708</span>
<span class="normal">709</span>
<span class="normal">710</span>
<span class="normal">711</span>
<span class="normal">712</span>
<span class="normal">713</span>
<span class="normal">714</span>
<span class="normal">715</span>
<span class="normal">716</span>
<span class="normal">717</span>
<span class="normal">718</span>
<span class="normal">719</span></pre></div></td><td class="code"><div><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">Dataset</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">,</span> <span class="n">Generic</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">],</span> <span class="n">extra</span><span class="o">=</span><span class="s1">'forbid'</span><span class="p">,</span> <span class="n">arbitrary_types_allowed</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A dataset of test [cases][pydantic_evals.Case].</span>

<span class="sd">    Datasets allow you to organize a collection of test cases and evaluate them against a task function.</span>
<span class="sd">    They can be loaded from and saved to YAML or JSON files, and can have dataset-level evaluators that</span>
<span class="sd">    apply to all cases.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    # Create a dataset with two test cases</span>
<span class="sd">    from dataclasses import dataclass</span>

<span class="sd">    from pydantic_evals import Case, Dataset</span>
<span class="sd">    from pydantic_evals.evaluators import Evaluator, EvaluatorContext</span>


<span class="sd">    @dataclass</span>
<span class="sd">    class ExactMatch(Evaluator):</span>
<span class="sd">        def evaluate(self, ctx: EvaluatorContext) -&gt; bool:</span>
<span class="sd">            return ctx.output == ctx.expected_output</span>

<span class="sd">    dataset = Dataset(</span>
<span class="sd">        cases=[</span>
<span class="sd">            Case(name='test1', inputs={'text': 'Hello'}, expected_output='HELLO'),</span>
<span class="sd">            Case(name='test2', inputs={'text': 'World'}, expected_output='WORLD'),</span>
<span class="sd">        ],</span>
<span class="sd">        evaluators=[ExactMatch()],</span>
<span class="sd">    )</span>

<span class="sd">    # Evaluate the dataset against a task function</span>
<span class="sd">    async def uppercase(inputs: dict) -&gt; str:</span>
<span class="sd">        return inputs['text'].upper()</span>

<span class="sd">    async def main():</span>
<span class="sd">        report = await dataset.evaluate(uppercase)</span>
<span class="sd">        report.print()</span>
<span class="sd">    '''</span>
<span class="sd">       Evaluation Summary: uppercase</span>
<span class="sd">    ┏━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓</span>
<span class="sd">    ┃ Case ID  ┃ Assertions ┃ Duration ┃</span>
<span class="sd">    ┡━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩</span>
<span class="sd">    │ test1    │ ✔          │     10ms │</span>
<span class="sd">    ├──────────┼────────────┼──────────┤</span>
<span class="sd">    │ test2    │ ✔          │     10ms │</span>
<span class="sd">    ├──────────┼────────────┼──────────┤</span>
<span class="sd">    │ Averages │ 100.0% ✔   │     10ms │</span>
<span class="sd">    └──────────┴────────────┴──────────┘</span>
<span class="sd">    '''</span>
<span class="sd">    ```</span>
<span class="sd">    """</span>

    <span class="n">cases</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Case</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]</span>
<span class="w">    </span><span class="sd">"""List of test cases in the dataset."""</span>
    <span class="n">evaluators</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>
<span class="w">    </span><span class="sd">"""List of evaluators to be used on all cases in the dataset."""</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">cases</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Case</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]],</span>
        <span class="n">evaluators</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize a new dataset with test cases and optional evaluators.</span>

<span class="sd">        Args:</span>
<span class="sd">            cases: Sequence of test cases to include in the dataset.</span>
<span class="sd">            evaluators: Optional sequence of evaluators to apply to all cases in the dataset.</span>
<span class="sd">        """</span>
        <span class="n">case_names</span> <span class="o">=</span> <span class="nb">set</span><span class="p">[</span><span class="nb">str</span><span class="p">]()</span>
        <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="k">if</span> <span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="ow">in</span> <span class="n">case_names</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Duplicate case name: </span><span class="si">{</span><span class="n">case</span><span class="o">.</span><span class="n">name</span><span class="si">!r}</span><span class="s1">'</span><span class="p">)</span>
            <span class="n">case_names</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">cases</span><span class="o">=</span><span class="n">cases</span><span class="p">,</span>
            <span class="n">evaluators</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="n">evaluators</span><span class="p">),</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">InputsT</span><span class="p">],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">OutputT</span><span class="p">]],</span> <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">max_concurrency</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationReport</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Evaluates the test cases in the dataset using the given task.</span>

<span class="sd">        This method runs the task on each case in the dataset, applies evaluators,</span>
<span class="sd">        and collects results into a report. Cases are run concurrently, limited by `max_concurrency` if specified.</span>

<span class="sd">        Args:</span>
<span class="sd">            task: The task to evaluate. This should be a callable that takes the inputs of the case</span>
<span class="sd">                and returns the output.</span>
<span class="sd">            name: The name of the task being evaluated, this is used to identify the task in the report.</span>
<span class="sd">                If omitted, the name of the task function will be used.</span>
<span class="sd">            max_concurrency: The maximum number of concurrent evaluations of the task to allow.</span>
<span class="sd">                If None, all cases will be evaluated concurrently.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A report containing the results of the evaluation.</span>
<span class="sd">        """</span>
        <span class="n">name</span> <span class="o">=</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">get_unwrapped_function_name</span><span class="p">(</span><span class="n">task</span><span class="p">)</span>

        <span class="n">limiter</span> <span class="o">=</span> <span class="n">anyio</span><span class="o">.</span><span class="n">Semaphore</span><span class="p">(</span><span class="n">max_concurrency</span><span class="p">)</span> <span class="k">if</span> <span class="n">max_concurrency</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">AsyncExitStack</span><span class="p">()</span>
        <span class="k">with</span> <span class="n">_logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'evaluate </span><span class="si">{name}</span><span class="s1">'</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">)</span> <span class="k">as</span> <span class="n">eval_span</span><span class="p">:</span>

            <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_handle_case</span><span class="p">(</span><span class="n">case</span><span class="p">:</span> <span class="n">Case</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">],</span> <span class="n">report_case_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
                <span class="k">async</span> <span class="k">with</span> <span class="n">limiter</span><span class="p">:</span>
                    <span class="k">return</span> <span class="k">await</span> <span class="n">_run_task_and_evaluators</span><span class="p">(</span><span class="n">task</span><span class="p">,</span> <span class="n">case</span><span class="p">,</span> <span class="n">report_case_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span><span class="p">)</span>

            <span class="n">report</span> <span class="o">=</span> <span class="n">EvaluationReport</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
                <span class="n">cases</span><span class="o">=</span><span class="k">await</span> <span class="n">task_group_gather</span><span class="p">(</span>
                    <span class="p">[</span>
                        <span class="k">lambda</span> <span class="n">case</span><span class="o">=</span><span class="n">case</span><span class="p">,</span> <span class="n">i</span><span class="o">=</span><span class="n">i</span><span class="p">:</span> <span class="n">_handle_case</span><span class="p">(</span><span class="n">case</span><span class="p">,</span> <span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="ow">or</span> <span class="sa">f</span><span class="s1">'Case </span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
                        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">case</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cases</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
                    <span class="p">]</span>
                <span class="p">),</span>
            <span class="p">)</span>
            <span class="c1"># TODO(DavidM): This attribute will be too big in general; remove it once we can use child spans in details panel:</span>
            <span class="n">eval_span</span><span class="o">.</span><span class="n">set_attribute</span><span class="p">(</span><span class="s1">'cases'</span><span class="p">,</span> <span class="n">report</span><span class="o">.</span><span class="n">cases</span><span class="p">)</span>
            <span class="c1"># TODO(DavidM): Remove this 'averages' attribute once we compute it in the details panel</span>
            <span class="n">eval_span</span><span class="o">.</span><span class="n">set_attribute</span><span class="p">(</span><span class="s1">'averages'</span><span class="p">,</span> <span class="n">report</span><span class="o">.</span><span class="n">averages</span><span class="p">())</span>

        <span class="k">return</span> <span class="n">report</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate_sync</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">InputsT</span><span class="p">],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">OutputT</span><span class="p">]],</span> <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">max_concurrency</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationReport</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
<span class="w">        </span><span class="sd">"""Evaluates the test cases in the dataset using the given task.</span>

<span class="sd">        This is a synchronous wrapper around [`evaluate`][pydantic_evals.Dataset.evaluate] provided for convenience.</span>

<span class="sd">        Args:</span>
<span class="sd">            task: The task to evaluate. This should be a callable that takes the inputs of the case</span>
<span class="sd">                and returns the output.</span>
<span class="sd">            name: The name of the task being evaluated, this is used to identify the task in the report.</span>
<span class="sd">                If omitted, the name of the task function will be used.</span>
<span class="sd">            max_concurrency: The maximum number of concurrent evaluations of the task to allow.</span>
<span class="sd">                If None, all cases will be evaluated concurrently.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A report containing the results of the evaluation.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">task</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">max_concurrency</span><span class="o">=</span><span class="n">max_concurrency</span><span class="p">))</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">add_case</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">inputs</span><span class="p">:</span> <span class="n">InputsT</span><span class="p">,</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">MetadataT</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">expected_output</span><span class="p">:</span> <span class="n">OutputT</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">evaluators</span><span class="p">:</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">],</span> <span class="o">...</span><span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Adds a case to the dataset.</span>

<span class="sd">        This is a convenience method for creating a [`Case`][pydantic_evals.Case] and adding it to the dataset.</span>

<span class="sd">        Args:</span>
<span class="sd">            name: Optional name for the case. If not provided, a generic name will be assigned.</span>
<span class="sd">            inputs: The inputs to the task being evaluated.</span>
<span class="sd">            metadata: Optional metadata for the case, which can be used by evaluators.</span>
<span class="sd">            expected_output: The expected output of the task, used for comparison in evaluators.</span>
<span class="sd">            evaluators: Tuple of evaluators specific to this case, in addition to dataset-level evaluators.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="p">{</span><span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">cases</span><span class="p">}:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Duplicate case name: </span><span class="si">{</span><span class="n">name</span><span class="si">!r}</span><span class="s1">'</span><span class="p">)</span>

        <span class="n">case</span> <span class="o">=</span> <span class="n">Case</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">](</span>
            <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
            <span class="n">inputs</span><span class="o">=</span><span class="n">inputs</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="n">expected_output</span><span class="o">=</span><span class="n">expected_output</span><span class="p">,</span>
            <span class="n">evaluators</span><span class="o">=</span><span class="n">evaluators</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cases</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">case</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">add_evaluator</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">evaluator</span><span class="p">:</span> <span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">],</span>
        <span class="n">specific_case</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Adds an evaluator to the dataset or a specific case.</span>

<span class="sd">        Args:</span>
<span class="sd">            evaluator: The evaluator to add.</span>
<span class="sd">            specific_case: If provided, the evaluator will only be added to the case with this name.</span>
<span class="sd">                If None, the evaluator will be added to all cases in the dataset.</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValueError: If `specific_case` is provided but no case with that name exists in the dataset.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">specific_case</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">evaluator</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># If this is too slow, we could try to add a case lookup dict.</span>
            <span class="c1"># Note that if we do that, we'd need to make the cases list private to prevent modification.</span>
            <span class="n">added</span> <span class="o">=</span> <span class="kc">False</span>
            <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">cases</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="n">specific_case</span><span class="p">:</span>
                    <span class="k">case</span><span class="o">.</span><span class="n">evaluators</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">evaluator</span><span class="p">)</span>
                    <span class="n">added</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">added</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Case </span><span class="si">{</span><span class="n">specific_case</span><span class="si">!r}</span><span class="s1"> not found in the dataset'</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="nd">@functools</span><span class="o">.</span><span class="n">cache</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_params</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">InputsT</span><span class="p">],</span> <span class="nb">type</span><span class="p">[</span><span class="n">OutputT</span><span class="p">],</span> <span class="nb">type</span><span class="p">[</span><span class="n">MetadataT</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get the type parameters for the Dataset class.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A tuple of (InputsT, OutputT, MetadataT) types.</span>
<span class="sd">        """</span>
        <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="bp">cls</span><span class="o">.</span><span class="vm">__mro__</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">c</span><span class="p">,</span> <span class="s1">'__pydantic_generic_metadata__'</span><span class="p">,</span> <span class="p">{})</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span> <span class="o">:=</span> <span class="p">(</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'args'</span><span class="p">,</span> <span class="p">())</span> <span class="ow">or</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">c</span><span class="p">,</span> <span class="s1">'__args__'</span><span class="p">,</span> <span class="p">())))</span> <span class="o">==</span> <span class="mi">3</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">args</span>
        <span class="k">else</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                <span class="sa">f</span><span class="s1">'Could not determine the generic parameters for </span><span class="si">{</span><span class="bp">cls</span><span class="si">}</span><span class="s1">; using `Any` for each. '</span>
                <span class="sa">f</span><span class="s1">'You should explicitly set the generic parameters via `Dataset[MyInputs, MyOutput, MyMetadata]`'</span>
                <span class="sa">f</span><span class="s1">'when serializing or deserializing.'</span><span class="p">,</span>
                <span class="ne">UserWarning</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span>  <span class="c1"># type: ignore</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">from_file</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">path</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">fmt</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'yaml'</span><span class="p">,</span> <span class="s1">'json'</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Self</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a dataset from a file.</span>

<span class="sd">        Args:</span>
<span class="sd">            path: Path to the file to load.</span>
<span class="sd">            fmt: Format of the file. If None, the format will be inferred from the file extension.</span>
<span class="sd">                Must be either 'yaml' or 'json'.</span>
<span class="sd">            custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.</span>
<span class="sd">                These are additional evaluators beyond the default ones.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A new Dataset instance loaded from the file.</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValidationError: If the file cannot be parsed as a valid dataset.</span>
<span class="sd">            ValueError: If the format cannot be inferred from the file extension.</span>
<span class="sd">        """</span>
        <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
        <span class="n">fmt</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_infer_fmt</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">fmt</span><span class="p">)</span>

        <span class="n">raw</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read_text</span><span class="p">()</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_text</span><span class="p">(</span><span class="n">raw</span><span class="p">,</span> <span class="n">fmt</span><span class="o">=</span><span class="n">fmt</span><span class="p">,</span> <span class="n">custom_evaluator_types</span><span class="o">=</span><span class="n">custom_evaluator_types</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">ValidationError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s1"> contains data that does not match the schema for </span><span class="si">{</span><span class="bp">cls</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">:</span><span class="se">\n</span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s1">.'</span><span class="p">)</span> <span class="kn">from</span><span class="w"> </span><span class="nn">e</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">from_text</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">contents</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">fmt</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'yaml'</span><span class="p">,</span> <span class="s1">'json'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'yaml'</span><span class="p">,</span>
        <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Self</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a dataset from a string.</span>

<span class="sd">        Args:</span>
<span class="sd">            contents: The string content to parse.</span>
<span class="sd">            fmt: Format of the content. Must be either 'yaml' or 'json'.</span>
<span class="sd">            custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.</span>
<span class="sd">                These are additional evaluators beyond the default ones.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A new Dataset instance parsed from the string.</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValidationError: If the content cannot be parsed as a valid dataset.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">fmt</span> <span class="o">==</span> <span class="s1">'yaml'</span><span class="p">:</span>
            <span class="n">loaded</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">contents</span><span class="p">)</span>
            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">loaded</span><span class="p">,</span> <span class="n">custom_evaluator_types</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">dataset_model_type</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_serialization_type</span><span class="p">()</span>
            <span class="n">dataset_model</span> <span class="o">=</span> <span class="n">dataset_model_type</span><span class="o">.</span><span class="n">model_validate_json</span><span class="p">(</span><span class="n">contents</span><span class="p">)</span>
            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_dataset_model</span><span class="p">(</span><span class="n">dataset_model</span><span class="p">,</span> <span class="n">custom_evaluator_types</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">from_dict</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">data</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
        <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Self</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a dataset from a dictionary.</span>

<span class="sd">        Args:</span>
<span class="sd">            data: Dictionary representation of the dataset.</span>
<span class="sd">            custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.</span>
<span class="sd">                These are additional evaluators beyond the default ones.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A new Dataset instance created from the dictionary.</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValidationError: If the dictionary cannot be converted to a valid dataset.</span>
<span class="sd">        """</span>
        <span class="n">dataset_model_type</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_serialization_type</span><span class="p">()</span>
        <span class="n">dataset_model</span> <span class="o">=</span> <span class="n">dataset_model_type</span><span class="o">.</span><span class="n">model_validate</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_dataset_model</span><span class="p">(</span><span class="n">dataset_model</span><span class="p">,</span> <span class="n">custom_evaluator_types</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_from_dataset_model</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">dataset_model</span><span class="p">:</span> <span class="n">_DatasetModel</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">],</span>
        <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Self</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a Dataset from a _DatasetModel.</span>

<span class="sd">        Args:</span>
<span class="sd">            dataset_model: The _DatasetModel to convert.</span>
<span class="sd">            custom_evaluator_types: Custom evaluator classes to register for deserialization.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A new Dataset instance created from the _DatasetModel.</span>
<span class="sd">        """</span>
        <span class="n">registry</span> <span class="o">=</span> <span class="n">_get_registry</span><span class="p">(</span><span class="n">custom_evaluator_types</span><span class="p">)</span>

        <span class="n">cases</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Case</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">errors</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="ne">ValueError</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">dataset_evaluators</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">spec</span> <span class="ow">in</span> <span class="n">dataset_model</span><span class="o">.</span><span class="n">evaluators</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">dataset_evaluator</span> <span class="o">=</span> <span class="n">_load_evaluator_from_registry</span><span class="p">(</span><span class="n">registry</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">spec</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="n">errors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>
                <span class="k">continue</span>
            <span class="n">dataset_evaluators</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dataset_evaluator</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">dataset_model</span><span class="o">.</span><span class="n">cases</span><span class="p">:</span>
            <span class="n">evaluators</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">spec</span> <span class="ow">in</span> <span class="n">row</span><span class="o">.</span><span class="n">evaluators</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">evaluator</span> <span class="o">=</span> <span class="n">_load_evaluator_from_registry</span><span class="p">(</span><span class="n">registry</span><span class="p">,</span> <span class="n">row</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">spec</span><span class="p">)</span>
                <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="n">errors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>
                    <span class="k">continue</span>
                <span class="n">evaluators</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">evaluator</span><span class="p">)</span>
            <span class="n">row</span> <span class="o">=</span> <span class="n">Case</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">](</span>
                <span class="n">name</span><span class="o">=</span><span class="n">row</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                <span class="n">inputs</span><span class="o">=</span><span class="n">row</span><span class="o">.</span><span class="n">inputs</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">row</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                <span class="n">expected_output</span><span class="o">=</span><span class="n">row</span><span class="o">.</span><span class="n">expected_output</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">row</span><span class="o">.</span><span class="n">evaluators</span> <span class="o">=</span> <span class="n">evaluators</span>
            <span class="n">cases</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">row</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">errors</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">ExceptionGroup</span><span class="p">(</span><span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">errors</span><span class="p">)</span><span class="si">}</span><span class="s1"> error(s) loading evaluators from registry'</span><span class="p">,</span> <span class="n">errors</span><span class="p">[:</span><span class="mi">3</span><span class="p">])</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="p">(</span><span class="n">cases</span><span class="o">=</span><span class="n">cases</span><span class="p">)</span>
        <span class="n">result</span><span class="o">.</span><span class="n">evaluators</span> <span class="o">=</span> <span class="n">dataset_evaluators</span>
        <span class="k">return</span> <span class="n">result</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">to_file</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">path</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">fmt</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'yaml'</span><span class="p">,</span> <span class="s1">'json'</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">schema_path</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">DEFAULT_SCHEMA_PATH_TEMPLATE</span><span class="p">,</span>
        <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Save the dataset to a file.</span>

<span class="sd">        Args:</span>
<span class="sd">            path: Path to save the dataset to.</span>
<span class="sd">            fmt: Format to use. If None, the format will be inferred from the file extension.</span>
<span class="sd">                Must be either 'yaml' or 'json'.</span>
<span class="sd">            schema_path: Path to save the JSON schema to. If None, no schema will be saved.</span>
<span class="sd">                Can be a string template with {stem} which will be replaced with the dataset filename stem.</span>
<span class="sd">            custom_evaluator_types: Custom evaluator classes to include in the schema.</span>
<span class="sd">        """</span>
        <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
        <span class="n">fmt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_infer_fmt</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">fmt</span><span class="p">)</span>

        <span class="n">schema_ref</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">schema_path</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">schema_path</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
                <span class="n">schema_path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">schema_path</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">stem</span><span class="o">=</span><span class="n">path</span><span class="o">.</span><span class="n">stem</span><span class="p">))</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="n">schema_path</span><span class="o">.</span><span class="n">is_absolute</span><span class="p">():</span>
                <span class="n">schema_ref</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">schema_path</span><span class="p">)</span>
                <span class="n">schema_path</span> <span class="o">=</span> <span class="n">path</span><span class="o">.</span><span class="n">parent</span> <span class="o">/</span> <span class="n">schema_path</span>
            <span class="k">elif</span> <span class="n">schema_path</span><span class="o">.</span><span class="n">is_relative_to</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>  <span class="c1"># pragma: no cover</span>
                <span class="n">schema_ref</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">_get_relative_path_reference</span><span class="p">(</span><span class="n">schema_path</span><span class="p">,</span> <span class="n">path</span><span class="p">))</span>
            <span class="k">else</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
                <span class="n">schema_ref</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">schema_path</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_save_schema</span><span class="p">(</span><span class="n">schema_path</span><span class="p">,</span> <span class="n">custom_evaluator_types</span><span class="p">)</span>

        <span class="n">context</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'use_short_form'</span><span class="p">:</span> <span class="kc">True</span><span class="p">}</span>
        <span class="k">if</span> <span class="n">fmt</span> <span class="o">==</span> <span class="s1">'yaml'</span><span class="p">:</span>
            <span class="n">dumped_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">model_dump</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s1">'json'</span><span class="p">,</span> <span class="n">by_alias</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">exclude_defaults</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">dumped_data</span><span class="p">,</span> <span class="n">sort_keys</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">schema_ref</span><span class="p">:</span>
                <span class="n">yaml_language_server_line</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">_YAML_SCHEMA_LINE_PREFIX</span><span class="si">}{</span><span class="n">schema_ref</span><span class="si">}</span><span class="s1">'</span>
                <span class="n">content</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">yaml_language_server_line</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">content</span><span class="si">}</span><span class="s1">'</span>
            <span class="n">path</span><span class="o">.</span><span class="n">write_text</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">context</span><span class="p">[</span><span class="s1">'$schema'</span><span class="p">]</span> <span class="o">=</span> <span class="n">schema_ref</span>
            <span class="n">json_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">model_dump_json</span><span class="p">(</span><span class="n">indent</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">by_alias</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">exclude_defaults</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
            <span class="n">path</span><span class="o">.</span><span class="n">write_text</span><span class="p">(</span><span class="n">json_data</span> <span class="o">+</span> <span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">model_json_schema_with_evaluators</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Generate a JSON schema for this dataset type, including evaluator details.</span>

<span class="sd">        This is useful for generating a schema that can be used to validate YAML-format dataset files.</span>

<span class="sd">        Args:</span>
<span class="sd">            custom_evaluator_types: Custom evaluator classes to include in the schema.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A dictionary representing the JSON schema.</span>
<span class="sd">        """</span>
        <span class="c1"># Note: this function could maybe be simplified now that Evaluators are always dataclasses</span>
        <span class="n">registry</span> <span class="o">=</span> <span class="n">_get_registry</span><span class="p">(</span><span class="n">custom_evaluator_types</span><span class="p">)</span>

        <span class="n">evaluator_schema_types</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">evaluator_class</span> <span class="ow">in</span> <span class="n">registry</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">type_hints</span> <span class="o">=</span> <span class="n">_typing_extra</span><span class="o">.</span><span class="n">get_function_type_hints</span><span class="p">(</span><span class="n">evaluator_class</span><span class="p">)</span>
            <span class="n">type_hints</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">'return'</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
            <span class="n">required_type_hints</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>

            <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">inspect</span><span class="o">.</span><span class="n">signature</span><span class="p">(</span><span class="n">evaluator_class</span><span class="p">)</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
                <span class="n">type_hints</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">Any</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">p</span><span class="o">.</span><span class="n">default</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">p</span><span class="o">.</span><span class="n">empty</span><span class="p">:</span>
                    <span class="n">type_hints</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">NotRequired</span><span class="p">[</span><span class="n">type_hints</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">name</span><span class="p">]]</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">required_type_hints</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">type_hints</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">name</span><span class="p">]</span>

            <span class="k">def</span><span class="w"> </span><span class="nf">_make_typed_dict</span><span class="p">(</span><span class="n">cls_name_prefix</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
                <span class="n">td</span> <span class="o">=</span> <span class="n">TypedDict</span><span class="p">(</span><span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">cls_name_prefix</span><span class="si">}</span><span class="s1">_</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span> <span class="n">fields</span><span class="p">)</span>  <span class="c1"># pyright: ignore[reportArgumentType]</span>
                <span class="n">config</span> <span class="o">=</span> <span class="n">ConfigDict</span><span class="p">(</span><span class="n">extra</span><span class="o">=</span><span class="s1">'forbid'</span><span class="p">,</span> <span class="n">arbitrary_types_allowed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
                <span class="c1"># TODO: Replace with pydantic.with_config after pydantic 2.11 is released</span>
                <span class="n">td</span><span class="o">.</span><span class="n">__pydantic_config__</span> <span class="o">=</span> <span class="n">config</span>  <span class="c1"># pyright: ignore[reportAttributeAccessIssue]</span>
                <span class="k">return</span> <span class="n">td</span>

            <span class="c1"># Shortest form: just the call name</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">type_hints</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">required_type_hints</span><span class="p">:</span>
                <span class="n">evaluator_schema_types</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Literal</span><span class="p">[</span><span class="n">name</span><span class="p">])</span>

            <span class="c1"># Short form: can be called with only one parameter</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">type_hints</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
                <span class="p">[</span><span class="n">type_hint_type</span><span class="p">]</span> <span class="o">=</span> <span class="n">type_hints</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
                <span class="n">evaluator_schema_types</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_make_typed_dict</span><span class="p">(</span><span class="s1">'short_evaluator'</span><span class="p">,</span> <span class="p">{</span><span class="n">name</span><span class="p">:</span> <span class="n">type_hint_type</span><span class="p">}))</span>
            <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">required_type_hints</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
                <span class="p">[</span><span class="n">type_hint_type</span><span class="p">]</span> <span class="o">=</span> <span class="n">required_type_hints</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
                <span class="n">evaluator_schema_types</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_make_typed_dict</span><span class="p">(</span><span class="s1">'short_evaluator'</span><span class="p">,</span> <span class="p">{</span><span class="n">name</span><span class="p">:</span> <span class="n">type_hint_type</span><span class="p">}))</span>

            <span class="c1"># Long form: multiple parameters, possibly required</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">type_hints</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="n">params_td</span> <span class="o">=</span> <span class="n">_make_typed_dict</span><span class="p">(</span><span class="s1">'evaluator_params'</span><span class="p">,</span> <span class="n">type_hints</span><span class="p">)</span>
                <span class="n">evaluator_schema_types</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_make_typed_dict</span><span class="p">(</span><span class="s1">'evaluator'</span><span class="p">,</span> <span class="p">{</span><span class="n">name</span><span class="p">:</span> <span class="n">params_td</span><span class="p">}))</span>

        <span class="n">in_type</span><span class="p">,</span> <span class="n">out_type</span><span class="p">,</span> <span class="n">meta_type</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_params</span><span class="p">()</span>

        <span class="c1"># Note: we shadow the `Case` and `Dataset` class names here to generate a clean JSON schema</span>
        <span class="k">class</span><span class="w"> </span><span class="nc">Case</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">,</span> <span class="n">extra</span><span class="o">=</span><span class="s1">'forbid'</span><span class="p">):</span>  <span class="c1"># pyright: ignore[reportUnusedClass]  # this _is_ used below, but pyright doesn't seem to notice..</span>
            <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="n">inputs</span><span class="p">:</span> <span class="n">in_type</span>  <span class="c1"># pyright: ignore[reportInvalidTypeForm]</span>
            <span class="n">metadata</span><span class="p">:</span> <span class="n">meta_type</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># pyright: ignore[reportInvalidTypeForm,reportUnknownVariableType]</span>
            <span class="n">expected_output</span><span class="p">:</span> <span class="n">out_type</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># pyright: ignore[reportInvalidTypeForm,reportUnknownVariableType]</span>
            <span class="k">if</span> <span class="n">evaluator_schema_types</span><span class="p">:</span>
                <span class="n">evaluators</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">tuple</span><span class="p">(</span><span class="n">evaluator_schema_types</span><span class="p">)]]</span> <span class="o">=</span> <span class="p">[]</span>  <span class="c1"># pyright: ignore  # noqa UP007</span>

        <span class="k">class</span><span class="w"> </span><span class="nc">Dataset</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">,</span> <span class="n">extra</span><span class="o">=</span><span class="s1">'forbid'</span><span class="p">):</span>
            <span class="n">cases</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Case</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">evaluator_schema_types</span><span class="p">:</span>
                <span class="n">evaluators</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">tuple</span><span class="p">(</span><span class="n">evaluator_schema_types</span><span class="p">)]]</span> <span class="o">=</span> <span class="p">[]</span>  <span class="c1"># pyright: ignore  # noqa UP007</span>

        <span class="n">json_schema</span> <span class="o">=</span> <span class="n">Dataset</span><span class="o">.</span><span class="n">model_json_schema</span><span class="p">()</span>
        <span class="c1"># See `_add_json_schema` below, since `$schema` is added to the JSON, it has to be supported in the JSON</span>
        <span class="n">json_schema</span><span class="p">[</span><span class="s1">'properties'</span><span class="p">][</span><span class="s1">'$schema'</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'type'</span><span class="p">:</span> <span class="s1">'string'</span><span class="p">}</span>
        <span class="k">return</span> <span class="n">json_schema</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_save_schema</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span><span class="p">,</span> <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">()</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Save the JSON schema for this dataset type to a file.</span>

<span class="sd">        Args:</span>
<span class="sd">            path: Path to save the schema to.</span>
<span class="sd">            custom_evaluator_types: Custom evaluator classes to include in the schema.</span>
<span class="sd">        """</span>
        <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
        <span class="n">json_schema</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="n">model_json_schema_with_evaluators</span><span class="p">(</span><span class="n">custom_evaluator_types</span><span class="p">)</span>
        <span class="n">schema_content</span> <span class="o">=</span> <span class="n">to_json</span><span class="p">(</span><span class="n">json_schema</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span> <span class="o">+</span> <span class="s1">'</span><span class="se">\n</span><span class="s1">'</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">()</span> <span class="ow">or</span> <span class="n">path</span><span class="o">.</span><span class="n">read_text</span><span class="p">()</span> <span class="o">!=</span> <span class="n">schema_content</span><span class="p">:</span>
            <span class="n">path</span><span class="o">.</span><span class="n">write_text</span><span class="p">(</span><span class="n">schema_content</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="nd">@functools</span><span class="o">.</span><span class="n">cache</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_serialization_type</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">type</span><span class="p">[</span><span class="n">_DatasetModel</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get the serialization type for this dataset class.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A _DatasetModel type with the same generic parameters as this Dataset class.</span>
<span class="sd">        """</span>
        <span class="n">input_type</span><span class="p">,</span> <span class="n">output_type</span><span class="p">,</span> <span class="n">metadata_type</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_params</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">_DatasetModel</span><span class="p">[</span><span class="n">input_type</span><span class="p">,</span> <span class="n">output_type</span><span class="p">,</span> <span class="n">metadata_type</span><span class="p">]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_infer_fmt</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">fmt</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'yaml'</span><span class="p">,</span> <span class="s1">'json'</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'yaml'</span><span class="p">,</span> <span class="s1">'json'</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Infer the format to use for a file based on its extension.</span>

<span class="sd">        Args:</span>
<span class="sd">            path: The path to infer the format for.</span>
<span class="sd">            fmt: The explicitly provided format, if any.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The inferred format ('yaml' or 'json').</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValueError: If the format cannot be inferred from the file extension.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">fmt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">fmt</span>
        <span class="n">suffix</span> <span class="o">=</span> <span class="n">path</span><span class="o">.</span><span class="n">suffix</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">suffix</span> <span class="ow">in</span> <span class="p">{</span><span class="s1">'.yaml'</span><span class="p">,</span> <span class="s1">'.yml'</span><span class="p">}:</span>
            <span class="k">return</span> <span class="s1">'yaml'</span>
        <span class="k">elif</span> <span class="n">suffix</span> <span class="o">==</span> <span class="s1">'.json'</span><span class="p">:</span>
            <span class="k">return</span> <span class="s1">'json'</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s1">'Could not infer format for filename </span><span class="si">{</span><span class="n">path</span><span class="o">.</span><span class="n">name</span><span class="si">!r}</span><span class="s1">. Use the `fmt` argument to specify the format.'</span>
        <span class="p">)</span>

    <span class="nd">@model_serializer</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s1">'wrap'</span><span class="p">)</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_add_json_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nxt</span><span class="p">:</span> <span class="n">SerializerFunctionWrapHandler</span><span class="p">,</span> <span class="n">info</span><span class="p">:</span> <span class="n">SerializationInfo</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add the JSON schema path to the serialized output.</span>

<span class="sd">        See &lt;https://github.com/json-schema-org/json-schema-spec/issues/828&gt; for context, that seems to be the nearest</span>
<span class="sd">        there is to a spec for this.</span>
<span class="sd">        """</span>
        <span class="n">context</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Union</span><span class="p">[</span><span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="kc">None</span><span class="p">],</span> <span class="n">info</span><span class="o">.</span><span class="n">context</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">context</span><span class="p">,</span> <span class="nb">dict</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">schema</span> <span class="o">:=</span> <span class="n">context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'$schema'</span><span class="p">)):</span>
            <span class="k">return</span> <span class="p">{</span><span class="s1">'$schema'</span><span class="p">:</span> <span class="n">schema</span><span class="p">}</span> <span class="o">|</span> <span class="n">nxt</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">nxt</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.dataset.Dataset.cases" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">cases</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="n">cases</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.dataset.Case" href="#pydantic_evals.dataset.Case">Case</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>List of test cases in the dataset.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.dataset.Dataset.evaluators" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">evaluators</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="n">evaluators</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">]]</span> <span class="o">=</span> <span class="p">(</span>
    <span class="p">[]</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>List of evaluators to be used on all cases in the dataset.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.dataset.Dataset.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">cases</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.dataset.Case" href="#pydantic_evals.dataset.Case">Case</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">]],</span>
    <span class="n">evaluators</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="p">()</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Initialize a new dataset with test cases and optional evaluators.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>cases</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.dataset.Case" href="#pydantic_evals.dataset.Case">Case</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Sequence of test cases to include in the dataset.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>evaluators</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional sequence of evaluators to apply to all cases in the dataset.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span></pre></div></td><td class="code"><div><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">cases</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Case</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]],</span>
    <span class="n">evaluators</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Initialize a new dataset with test cases and optional evaluators.</span>

<span class="sd">    Args:</span>
<span class="sd">        cases: Sequence of test cases to include in the dataset.</span>
<span class="sd">        evaluators: Optional sequence of evaluators to apply to all cases in the dataset.</span>
<span class="sd">    """</span>
    <span class="n">case_names</span> <span class="o">=</span> <span class="nb">set</span><span class="p">[</span><span class="nb">str</span><span class="p">]()</span>
    <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">continue</span>
        <span class="k">if</span> <span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="ow">in</span> <span class="n">case_names</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Duplicate case name: </span><span class="si">{</span><span class="n">case</span><span class="o">.</span><span class="n">name</span><span class="si">!r}</span><span class="s1">'</span><span class="p">)</span>
        <span class="n">case_names</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>

    <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
        <span class="n">cases</span><span class="o">=</span><span class="n">cases</span><span class="p">,</span>
        <span class="n">evaluators</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="n">evaluators</span><span class="p">),</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.dataset.Dataset.evaluate" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">evaluate</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="nf">evaluate</span><span class="p">(</span>
    <span class="n">task</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">]],</span>
    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">max_concurrency</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.EvaluationReport" href="../reporting/#pydantic_evals.reporting.EvaluationReport">EvaluationReport</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Evaluates the test cases in the dataset using the given task.</p>
<p>This method runs the task on each case in the dataset, applies evaluators,
and collects results into a report. Cases are run concurrently, limited by <code>max_concurrency</code> if specified.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>task</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a>[[<span title="pydantic_evals.dataset.InputsT">InputsT</span>], <a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a>[<span title="pydantic_evals.dataset.OutputT">OutputT</span>]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The task to evaluate. This should be a callable that takes the inputs of the case
and returns the output.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name of the task being evaluated, this is used to identify the task in the report.
If omitted, the name of the task function will be used.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>max_concurrency</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The maximum number of concurrent evaluations of the task to allow.
If None, all cases will be evaluated concurrently.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.EvaluationReport" href="../reporting/#pydantic_evals.reporting.EvaluationReport">EvaluationReport</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A report containing the results of the evaluation.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span></pre></div></td><td class="code"><div><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code tabindex="0"><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">InputsT</span><span class="p">],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">OutputT</span><span class="p">]],</span> <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">max_concurrency</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationReport</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Evaluates the test cases in the dataset using the given task.</span>

<span class="sd">    This method runs the task on each case in the dataset, applies evaluators,</span>
<span class="sd">    and collects results into a report. Cases are run concurrently, limited by `max_concurrency` if specified.</span>

<span class="sd">    Args:</span>
<span class="sd">        task: The task to evaluate. This should be a callable that takes the inputs of the case</span>
<span class="sd">            and returns the output.</span>
<span class="sd">        name: The name of the task being evaluated, this is used to identify the task in the report.</span>
<span class="sd">            If omitted, the name of the task function will be used.</span>
<span class="sd">        max_concurrency: The maximum number of concurrent evaluations of the task to allow.</span>
<span class="sd">            If None, all cases will be evaluated concurrently.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A report containing the results of the evaluation.</span>
<span class="sd">    """</span>
    <span class="n">name</span> <span class="o">=</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">get_unwrapped_function_name</span><span class="p">(</span><span class="n">task</span><span class="p">)</span>

    <span class="n">limiter</span> <span class="o">=</span> <span class="n">anyio</span><span class="o">.</span><span class="n">Semaphore</span><span class="p">(</span><span class="n">max_concurrency</span><span class="p">)</span> <span class="k">if</span> <span class="n">max_concurrency</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">AsyncExitStack</span><span class="p">()</span>
    <span class="k">with</span> <span class="n">_logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'evaluate </span><span class="si">{name}</span><span class="s1">'</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">)</span> <span class="k">as</span> <span class="n">eval_span</span><span class="p">:</span>

        <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_handle_case</span><span class="p">(</span><span class="n">case</span><span class="p">:</span> <span class="n">Case</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">],</span> <span class="n">report_case_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">async</span> <span class="k">with</span> <span class="n">limiter</span><span class="p">:</span>
                <span class="k">return</span> <span class="k">await</span> <span class="n">_run_task_and_evaluators</span><span class="p">(</span><span class="n">task</span><span class="p">,</span> <span class="n">case</span><span class="p">,</span> <span class="n">report_case_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span><span class="p">)</span>

        <span class="n">report</span> <span class="o">=</span> <span class="n">EvaluationReport</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
            <span class="n">cases</span><span class="o">=</span><span class="k">await</span> <span class="n">task_group_gather</span><span class="p">(</span>
                <span class="p">[</span>
                    <span class="k">lambda</span> <span class="n">case</span><span class="o">=</span><span class="n">case</span><span class="p">,</span> <span class="n">i</span><span class="o">=</span><span class="n">i</span><span class="p">:</span> <span class="n">_handle_case</span><span class="p">(</span><span class="n">case</span><span class="p">,</span> <span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="ow">or</span> <span class="sa">f</span><span class="s1">'Case </span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
                    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">case</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cases</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
                <span class="p">]</span>
            <span class="p">),</span>
        <span class="p">)</span>
        <span class="c1"># TODO(DavidM): This attribute will be too big in general; remove it once we can use child spans in details panel:</span>
        <span class="n">eval_span</span><span class="o">.</span><span class="n">set_attribute</span><span class="p">(</span><span class="s1">'cases'</span><span class="p">,</span> <span class="n">report</span><span class="o">.</span><span class="n">cases</span><span class="p">)</span>
        <span class="c1"># TODO(DavidM): Remove this 'averages' attribute once we compute it in the details panel</span>
        <span class="n">eval_span</span><span class="o">.</span><span class="n">set_attribute</span><span class="p">(</span><span class="s1">'averages'</span><span class="p">,</span> <span class="n">report</span><span class="o">.</span><span class="n">averages</span><span class="p">())</span>

    <span class="k">return</span> <span class="n">report</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.dataset.Dataset.evaluate_sync" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">evaluate_sync</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="nf">evaluate_sync</span><span class="p">(</span>
    <span class="n">task</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">]],</span>
    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">max_concurrency</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.EvaluationReport" href="../reporting/#pydantic_evals.reporting.EvaluationReport">EvaluationReport</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Evaluates the test cases in the dataset using the given task.</p>
<p>This is a synchronous wrapper around <a class="autorefs autorefs-internal" href="#pydantic_evals.dataset.Dataset.evaluate"><code>evaluate</code></a> provided for convenience.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>task</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a>[[<span title="pydantic_evals.dataset.InputsT">InputsT</span>], <a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a>[<span title="pydantic_evals.dataset.OutputT">OutputT</span>]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The task to evaluate. This should be a callable that takes the inputs of the case
and returns the output.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name of the task being evaluated, this is used to identify the task in the report.
If omitted, the name of the task function will be used.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>max_concurrency</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The maximum number of concurrent evaluations of the task to allow.
If None, all cases will be evaluated concurrently.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.EvaluationReport" href="../reporting/#pydantic_evals.reporting.EvaluationReport">EvaluationReport</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A report containing the results of the evaluation.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span></pre></div></td><td class="code"><div><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">evaluate_sync</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">InputsT</span><span class="p">],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">OutputT</span><span class="p">]],</span> <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">max_concurrency</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationReport</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
<span class="w">    </span><span class="sd">"""Evaluates the test cases in the dataset using the given task.</span>

<span class="sd">    This is a synchronous wrapper around [`evaluate`][pydantic_evals.Dataset.evaluate] provided for convenience.</span>

<span class="sd">    Args:</span>
<span class="sd">        task: The task to evaluate. This should be a callable that takes the inputs of the case</span>
<span class="sd">            and returns the output.</span>
<span class="sd">        name: The name of the task being evaluated, this is used to identify the task in the report.</span>
<span class="sd">            If omitted, the name of the task function will be used.</span>
<span class="sd">        max_concurrency: The maximum number of concurrent evaluations of the task to allow.</span>
<span class="sd">            If None, all cases will be evaluated concurrently.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A report containing the results of the evaluation.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">task</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">max_concurrency</span><span class="o">=</span><span class="n">max_concurrency</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.dataset.Dataset.add_case" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">add_case</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="nf">add_case</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">inputs</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">expected_output</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">evaluators</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple">tuple</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">],</span> <span class="o">...</span>
    <span class="p">]</span> <span class="o">=</span> <span class="p">()</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Adds a case to the dataset.</p>
<p>This is a convenience method for creating a <a class="autorefs autorefs-internal" href="#pydantic_evals.dataset.Case"><code>Case</code></a> and adding it to the dataset.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional name for the case. If not provided, a generic name will be assigned.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>inputs</code>
            </td>
            <td>
                  <code><span title="pydantic_evals.dataset.InputsT">InputsT</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The inputs to the task being evaluated.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>metadata</code>
            </td>
            <td>
                  <code><span title="pydantic_evals.dataset.MetadataT">MetadataT</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional metadata for the case, which can be used by evaluators.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>expected_output</code>
            </td>
            <td>
                  <code><span title="pydantic_evals.dataset.OutputT">OutputT</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The expected output of the task, used for comparison in evaluators.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>evaluators</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple">tuple</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>], ...]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Tuple of evaluators specific to this case, in addition to dataset-level evaluators.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span></pre></div></td><td class="code"><div><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">add_case</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">inputs</span><span class="p">:</span> <span class="n">InputsT</span><span class="p">,</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">MetadataT</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">expected_output</span><span class="p">:</span> <span class="n">OutputT</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">evaluators</span><span class="p">:</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">],</span> <span class="o">...</span><span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Adds a case to the dataset.</span>

<span class="sd">    This is a convenience method for creating a [`Case`][pydantic_evals.Case] and adding it to the dataset.</span>

<span class="sd">    Args:</span>
<span class="sd">        name: Optional name for the case. If not provided, a generic name will be assigned.</span>
<span class="sd">        inputs: The inputs to the task being evaluated.</span>
<span class="sd">        metadata: Optional metadata for the case, which can be used by evaluators.</span>
<span class="sd">        expected_output: The expected output of the task, used for comparison in evaluators.</span>
<span class="sd">        evaluators: Tuple of evaluators specific to this case, in addition to dataset-level evaluators.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="p">{</span><span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">cases</span><span class="p">}:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Duplicate case name: </span><span class="si">{</span><span class="n">name</span><span class="si">!r}</span><span class="s1">'</span><span class="p">)</span>

    <span class="n">case</span> <span class="o">=</span> <span class="n">Case</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">](</span>
        <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
        <span class="n">inputs</span><span class="o">=</span><span class="n">inputs</span><span class="p">,</span>
        <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
        <span class="n">expected_output</span><span class="o">=</span><span class="n">expected_output</span><span class="p">,</span>
        <span class="n">evaluators</span><span class="o">=</span><span class="n">evaluators</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">cases</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">case</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.dataset.Dataset.add_evaluator" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">add_evaluator</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code><span class="nf">add_evaluator</span><span class="p">(</span>
    <span class="n">evaluator</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">],</span>
    <span class="n">specific_case</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Adds an evaluator to the dataset or a specific case.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>evaluator</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The evaluator to add.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>specific_case</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If provided, the evaluator will only be added to the case with this name.
If None, the evaluator will be added to all cases in the dataset.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


<p><span class="doc-section-title">Raises:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#ValueError">ValueError</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If <code>specific_case</code> is provided but no case with that name exists in the dataset.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span></pre></div></td><td class="code"><div><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">add_evaluator</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">evaluator</span><span class="p">:</span> <span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">],</span>
    <span class="n">specific_case</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Adds an evaluator to the dataset or a specific case.</span>

<span class="sd">    Args:</span>
<span class="sd">        evaluator: The evaluator to add.</span>
<span class="sd">        specific_case: If provided, the evaluator will only be added to the case with this name.</span>
<span class="sd">            If None, the evaluator will be added to all cases in the dataset.</span>

<span class="sd">    Raises:</span>
<span class="sd">        ValueError: If `specific_case` is provided but no case with that name exists in the dataset.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">specific_case</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">evaluator</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># If this is too slow, we could try to add a case lookup dict.</span>
        <span class="c1"># Note that if we do that, we'd need to make the cases list private to prevent modification.</span>
        <span class="n">added</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">cases</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="n">specific_case</span><span class="p">:</span>
                <span class="k">case</span><span class="o">.</span><span class="n">evaluators</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">evaluator</span><span class="p">)</span>
                <span class="n">added</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">added</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Case </span><span class="si">{</span><span class="n">specific_case</span><span class="si">!r}</span><span class="s1"> not found in the dataset'</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>










<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.dataset.Dataset.from_file" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">from_file</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-classmethod"><code>classmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code><span class="nf">from_file</span><span class="p">(</span>
    <span class="n">path</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span>
    <span class="n">fmt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s2">"yaml"</span><span class="p">,</span> <span class="s2">"json"</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">]]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.Self" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self">Self</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Load a dataset from a file.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>path</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Path to the file to load.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>fmt</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a>['yaml', 'json'] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Format of the file. If None, the format will be inferred from the file extension.
Must be either 'yaml' or 'json'.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>custom_evaluator_types</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>]]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Custom evaluator classes to use when deserializing the dataset.
These are additional evaluators beyond the default ones.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" title="typing_extensions.Self" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self">Self</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A new Dataset instance loaded from the file.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>


<p><span class="doc-section-title">Raises:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><span title="pydantic.ValidationError">ValidationError</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If the file cannot be parsed as a valid dataset.</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#ValueError">ValueError</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If the format cannot be inferred from the file extension.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span></pre></div></td><td class="code"><div><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code tabindex="0"><span class="nd">@classmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">from_file</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">path</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">fmt</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'yaml'</span><span class="p">,</span> <span class="s1">'json'</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Self</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a dataset from a file.</span>

<span class="sd">    Args:</span>
<span class="sd">        path: Path to the file to load.</span>
<span class="sd">        fmt: Format of the file. If None, the format will be inferred from the file extension.</span>
<span class="sd">            Must be either 'yaml' or 'json'.</span>
<span class="sd">        custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.</span>
<span class="sd">            These are additional evaluators beyond the default ones.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A new Dataset instance loaded from the file.</span>

<span class="sd">    Raises:</span>
<span class="sd">        ValidationError: If the file cannot be parsed as a valid dataset.</span>
<span class="sd">        ValueError: If the format cannot be inferred from the file extension.</span>
<span class="sd">    """</span>
    <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
    <span class="n">fmt</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_infer_fmt</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">fmt</span><span class="p">)</span>

    <span class="n">raw</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read_text</span><span class="p">()</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_text</span><span class="p">(</span><span class="n">raw</span><span class="p">,</span> <span class="n">fmt</span><span class="o">=</span><span class="n">fmt</span><span class="p">,</span> <span class="n">custom_evaluator_types</span><span class="o">=</span><span class="n">custom_evaluator_types</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">ValidationError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s1"> contains data that does not match the schema for </span><span class="si">{</span><span class="bp">cls</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">:</span><span class="se">\n</span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s1">.'</span><span class="p">)</span> <span class="kn">from</span><span class="w"> </span><span class="nn">e</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.dataset.Dataset.from_text" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">from_text</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-classmethod"><code>classmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="nf">from_text</span><span class="p">(</span>
    <span class="n">contents</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span>
    <span class="n">fmt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s2">"yaml"</span><span class="p">,</span> <span class="s2">"json"</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"yaml"</span><span class="p">,</span>
    <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">]]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.Self" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self">Self</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Load a dataset from a string.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>contents</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The string content to parse.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>fmt</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a>['yaml', 'json']</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Format of the content. Must be either 'yaml' or 'json'.</p>
              </div>
            </td>
            <td>
                  <code>'yaml'</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>custom_evaluator_types</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>]]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Custom evaluator classes to use when deserializing the dataset.
These are additional evaluators beyond the default ones.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" title="typing_extensions.Self" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self">Self</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A new Dataset instance parsed from the string.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>


<p><span class="doc-section-title">Raises:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><span title="pydantic.ValidationError">ValidationError</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If the content cannot be parsed as a valid dataset.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span></pre></div></td><td class="code"><div><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="nd">@classmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">from_text</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">contents</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">fmt</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'yaml'</span><span class="p">,</span> <span class="s1">'json'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'yaml'</span><span class="p">,</span>
    <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Self</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a dataset from a string.</span>

<span class="sd">    Args:</span>
<span class="sd">        contents: The string content to parse.</span>
<span class="sd">        fmt: Format of the content. Must be either 'yaml' or 'json'.</span>
<span class="sd">        custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.</span>
<span class="sd">            These are additional evaluators beyond the default ones.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A new Dataset instance parsed from the string.</span>

<span class="sd">    Raises:</span>
<span class="sd">        ValidationError: If the content cannot be parsed as a valid dataset.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">fmt</span> <span class="o">==</span> <span class="s1">'yaml'</span><span class="p">:</span>
        <span class="n">loaded</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">contents</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">loaded</span><span class="p">,</span> <span class="n">custom_evaluator_types</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">dataset_model_type</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_serialization_type</span><span class="p">()</span>
        <span class="n">dataset_model</span> <span class="o">=</span> <span class="n">dataset_model_type</span><span class="o">.</span><span class="n">model_validate_json</span><span class="p">(</span><span class="n">contents</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_dataset_model</span><span class="p">(</span><span class="n">dataset_model</span><span class="p">,</span> <span class="n">custom_evaluator_types</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.dataset.Dataset.from_dict" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">from_dict</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-classmethod"><code>classmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_27"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_27 > code"></button><code><span class="nf">from_dict</span><span class="p">(</span>
    <span class="n">data</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">],</span>
    <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">]]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.Self" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self">Self</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Load a dataset from a dictionary.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>data</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Dictionary representation of the dataset.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>custom_evaluator_types</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>]]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Custom evaluator classes to use when deserializing the dataset.
These are additional evaluators beyond the default ones.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" title="typing_extensions.Self" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self">Self</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A new Dataset instance created from the dictionary.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>


<p><span class="doc-section-title">Raises:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><span title="pydantic.ValidationError">ValidationError</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If the dictionary cannot be converted to a valid dataset.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span></pre></div></td><td class="code"><div><pre id="__code_28"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_28 > code"></button><code><span class="nd">@classmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">from_dict</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">data</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Self</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a dataset from a dictionary.</span>

<span class="sd">    Args:</span>
<span class="sd">        data: Dictionary representation of the dataset.</span>
<span class="sd">        custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.</span>
<span class="sd">            These are additional evaluators beyond the default ones.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A new Dataset instance created from the dictionary.</span>

<span class="sd">    Raises:</span>
<span class="sd">        ValidationError: If the dictionary cannot be converted to a valid dataset.</span>
<span class="sd">    """</span>
    <span class="n">dataset_model_type</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_serialization_type</span><span class="p">()</span>
    <span class="n">dataset_model</span> <span class="o">=</span> <span class="n">dataset_model_type</span><span class="o">.</span><span class="n">model_validate</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_dataset_model</span><span class="p">(</span><span class="n">dataset_model</span><span class="p">,</span> <span class="n">custom_evaluator_types</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>










<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.dataset.Dataset.to_file" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">to_file</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_29"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_29 > code"></button><code><span class="nf">to_file</span><span class="p">(</span>
    <span class="n">path</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span>
    <span class="n">fmt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s2">"yaml"</span><span class="p">,</span> <span class="s2">"json"</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">schema_path</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="n"><span title="pydantic_evals.dataset.DEFAULT_SCHEMA_PATH_TEMPLATE">DEFAULT_SCHEMA_PATH_TEMPLATE</span></span><span class="p">,</span>
    <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">]]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Save the dataset to a file.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>path</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Path to save the dataset to.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>fmt</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a>['yaml', 'json'] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Format to use. If None, the format will be inferred from the file extension.
Must be either 'yaml' or 'json'.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>schema_path</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Path to save the JSON schema to. If None, no schema will be saved.
Can be a string template with {stem} which will be replaced with the dataset filename stem.</p>
              </div>
            </td>
            <td>
                  <code><span title="pydantic_evals.dataset.DEFAULT_SCHEMA_PATH_TEMPLATE">DEFAULT_SCHEMA_PATH_TEMPLATE</span></code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>custom_evaluator_types</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>]]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Custom evaluator classes to include in the schema.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span></pre></div></td><td class="code"><div><pre id="__code_30"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_30 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">to_file</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">path</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">fmt</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'yaml'</span><span class="p">,</span> <span class="s1">'json'</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">schema_path</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">DEFAULT_SCHEMA_PATH_TEMPLATE</span><span class="p">,</span>
    <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Save the dataset to a file.</span>

<span class="sd">    Args:</span>
<span class="sd">        path: Path to save the dataset to.</span>
<span class="sd">        fmt: Format to use. If None, the format will be inferred from the file extension.</span>
<span class="sd">            Must be either 'yaml' or 'json'.</span>
<span class="sd">        schema_path: Path to save the JSON schema to. If None, no schema will be saved.</span>
<span class="sd">            Can be a string template with {stem} which will be replaced with the dataset filename stem.</span>
<span class="sd">        custom_evaluator_types: Custom evaluator classes to include in the schema.</span>
<span class="sd">    """</span>
    <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
    <span class="n">fmt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_infer_fmt</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">fmt</span><span class="p">)</span>

    <span class="n">schema_ref</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">schema_path</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">schema_path</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">schema_path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">schema_path</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">stem</span><span class="o">=</span><span class="n">path</span><span class="o">.</span><span class="n">stem</span><span class="p">))</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">schema_path</span><span class="o">.</span><span class="n">is_absolute</span><span class="p">():</span>
            <span class="n">schema_ref</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">schema_path</span><span class="p">)</span>
            <span class="n">schema_path</span> <span class="o">=</span> <span class="n">path</span><span class="o">.</span><span class="n">parent</span> <span class="o">/</span> <span class="n">schema_path</span>
        <span class="k">elif</span> <span class="n">schema_path</span><span class="o">.</span><span class="n">is_relative_to</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>  <span class="c1"># pragma: no cover</span>
            <span class="n">schema_ref</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">_get_relative_path_reference</span><span class="p">(</span><span class="n">schema_path</span><span class="p">,</span> <span class="n">path</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
            <span class="n">schema_ref</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">schema_path</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_save_schema</span><span class="p">(</span><span class="n">schema_path</span><span class="p">,</span> <span class="n">custom_evaluator_types</span><span class="p">)</span>

    <span class="n">context</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'use_short_form'</span><span class="p">:</span> <span class="kc">True</span><span class="p">}</span>
    <span class="k">if</span> <span class="n">fmt</span> <span class="o">==</span> <span class="s1">'yaml'</span><span class="p">:</span>
        <span class="n">dumped_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">model_dump</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s1">'json'</span><span class="p">,</span> <span class="n">by_alias</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">exclude_defaults</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
        <span class="n">content</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">dumped_data</span><span class="p">,</span> <span class="n">sort_keys</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">schema_ref</span><span class="p">:</span>
            <span class="n">yaml_language_server_line</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">_YAML_SCHEMA_LINE_PREFIX</span><span class="si">}{</span><span class="n">schema_ref</span><span class="si">}</span><span class="s1">'</span>
            <span class="n">content</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">yaml_language_server_line</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">content</span><span class="si">}</span><span class="s1">'</span>
        <span class="n">path</span><span class="o">.</span><span class="n">write_text</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">context</span><span class="p">[</span><span class="s1">'$schema'</span><span class="p">]</span> <span class="o">=</span> <span class="n">schema_ref</span>
        <span class="n">json_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">model_dump_json</span><span class="p">(</span><span class="n">indent</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">by_alias</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">exclude_defaults</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
        <span class="n">path</span><span class="o">.</span><span class="n">write_text</span><span class="p">(</span><span class="n">json_data</span> <span class="o">+</span> <span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.dataset.Dataset.model_json_schema_with_evaluators" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">model_json_schema_with_evaluators</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-classmethod"><code>classmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_31"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_31 > code"></button><code><span class="nf">model_json_schema_with_evaluators</span><span class="p">(</span>
    <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.dataset.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.dataset.MetadataT">MetadataT</span></span><span class="p">]]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Generate a JSON schema for this dataset type, including evaluator details.</p>
<p>This is useful for generating a schema that can be used to validate YAML-format dataset files.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>custom_evaluator_types</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.Evaluator" href="../evaluators/#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<span title="pydantic_evals.dataset.InputsT">InputsT</span>, <span title="pydantic_evals.dataset.OutputT">OutputT</span>, <span title="pydantic_evals.dataset.MetadataT">MetadataT</span>]]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Custom evaluator classes to include in the schema.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A dictionary representing the JSON schema.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span>
<span class="normal">612</span>
<span class="normal">613</span>
<span class="normal">614</span>
<span class="normal">615</span>
<span class="normal">616</span>
<span class="normal">617</span>
<span class="normal">618</span>
<span class="normal">619</span>
<span class="normal">620</span>
<span class="normal">621</span>
<span class="normal">622</span>
<span class="normal">623</span>
<span class="normal">624</span>
<span class="normal">625</span>
<span class="normal">626</span>
<span class="normal">627</span>
<span class="normal">628</span>
<span class="normal">629</span>
<span class="normal">630</span>
<span class="normal">631</span>
<span class="normal">632</span>
<span class="normal">633</span>
<span class="normal">634</span>
<span class="normal">635</span>
<span class="normal">636</span>
<span class="normal">637</span>
<span class="normal">638</span>
<span class="normal">639</span>
<span class="normal">640</span>
<span class="normal">641</span>
<span class="normal">642</span>
<span class="normal">643</span>
<span class="normal">644</span>
<span class="normal">645</span>
<span class="normal">646</span>
<span class="normal">647</span>
<span class="normal">648</span>
<span class="normal">649</span>
<span class="normal">650</span>
<span class="normal">651</span>
<span class="normal">652</span>
<span class="normal">653</span>
<span class="normal">654</span></pre></div></td><td class="code"><div><pre id="__code_32"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_32 > code"></button><code tabindex="0"><span class="nd">@classmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">model_json_schema_with_evaluators</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">custom_evaluator_types</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">Evaluator</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">(),</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Generate a JSON schema for this dataset type, including evaluator details.</span>

<span class="sd">    This is useful for generating a schema that can be used to validate YAML-format dataset files.</span>

<span class="sd">    Args:</span>
<span class="sd">        custom_evaluator_types: Custom evaluator classes to include in the schema.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A dictionary representing the JSON schema.</span>
<span class="sd">    """</span>
    <span class="c1"># Note: this function could maybe be simplified now that Evaluators are always dataclasses</span>
    <span class="n">registry</span> <span class="o">=</span> <span class="n">_get_registry</span><span class="p">(</span><span class="n">custom_evaluator_types</span><span class="p">)</span>

    <span class="n">evaluator_schema_types</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">evaluator_class</span> <span class="ow">in</span> <span class="n">registry</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="n">type_hints</span> <span class="o">=</span> <span class="n">_typing_extra</span><span class="o">.</span><span class="n">get_function_type_hints</span><span class="p">(</span><span class="n">evaluator_class</span><span class="p">)</span>
        <span class="n">type_hints</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">'return'</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">required_type_hints</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">inspect</span><span class="o">.</span><span class="n">signature</span><span class="p">(</span><span class="n">evaluator_class</span><span class="p">)</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
            <span class="n">type_hints</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">Any</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">p</span><span class="o">.</span><span class="n">default</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">p</span><span class="o">.</span><span class="n">empty</span><span class="p">:</span>
                <span class="n">type_hints</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">NotRequired</span><span class="p">[</span><span class="n">type_hints</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">name</span><span class="p">]]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">required_type_hints</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">type_hints</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">name</span><span class="p">]</span>

        <span class="k">def</span><span class="w"> </span><span class="nf">_make_typed_dict</span><span class="p">(</span><span class="n">cls_name_prefix</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
            <span class="n">td</span> <span class="o">=</span> <span class="n">TypedDict</span><span class="p">(</span><span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">cls_name_prefix</span><span class="si">}</span><span class="s1">_</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span> <span class="n">fields</span><span class="p">)</span>  <span class="c1"># pyright: ignore[reportArgumentType]</span>
            <span class="n">config</span> <span class="o">=</span> <span class="n">ConfigDict</span><span class="p">(</span><span class="n">extra</span><span class="o">=</span><span class="s1">'forbid'</span><span class="p">,</span> <span class="n">arbitrary_types_allowed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="c1"># TODO: Replace with pydantic.with_config after pydantic 2.11 is released</span>
            <span class="n">td</span><span class="o">.</span><span class="n">__pydantic_config__</span> <span class="o">=</span> <span class="n">config</span>  <span class="c1"># pyright: ignore[reportAttributeAccessIssue]</span>
            <span class="k">return</span> <span class="n">td</span>

        <span class="c1"># Shortest form: just the call name</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">type_hints</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">required_type_hints</span><span class="p">:</span>
            <span class="n">evaluator_schema_types</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Literal</span><span class="p">[</span><span class="n">name</span><span class="p">])</span>

        <span class="c1"># Short form: can be called with only one parameter</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">type_hints</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
            <span class="p">[</span><span class="n">type_hint_type</span><span class="p">]</span> <span class="o">=</span> <span class="n">type_hints</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
            <span class="n">evaluator_schema_types</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_make_typed_dict</span><span class="p">(</span><span class="s1">'short_evaluator'</span><span class="p">,</span> <span class="p">{</span><span class="n">name</span><span class="p">:</span> <span class="n">type_hint_type</span><span class="p">}))</span>
        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">required_type_hints</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
            <span class="p">[</span><span class="n">type_hint_type</span><span class="p">]</span> <span class="o">=</span> <span class="n">required_type_hints</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
            <span class="n">evaluator_schema_types</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_make_typed_dict</span><span class="p">(</span><span class="s1">'short_evaluator'</span><span class="p">,</span> <span class="p">{</span><span class="n">name</span><span class="p">:</span> <span class="n">type_hint_type</span><span class="p">}))</span>

        <span class="c1"># Long form: multiple parameters, possibly required</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">type_hints</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">params_td</span> <span class="o">=</span> <span class="n">_make_typed_dict</span><span class="p">(</span><span class="s1">'evaluator_params'</span><span class="p">,</span> <span class="n">type_hints</span><span class="p">)</span>
            <span class="n">evaluator_schema_types</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_make_typed_dict</span><span class="p">(</span><span class="s1">'evaluator'</span><span class="p">,</span> <span class="p">{</span><span class="n">name</span><span class="p">:</span> <span class="n">params_td</span><span class="p">}))</span>

    <span class="n">in_type</span><span class="p">,</span> <span class="n">out_type</span><span class="p">,</span> <span class="n">meta_type</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_params</span><span class="p">()</span>

    <span class="c1"># Note: we shadow the `Case` and `Dataset` class names here to generate a clean JSON schema</span>
    <span class="k">class</span><span class="w"> </span><span class="nc">Case</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">,</span> <span class="n">extra</span><span class="o">=</span><span class="s1">'forbid'</span><span class="p">):</span>  <span class="c1"># pyright: ignore[reportUnusedClass]  # this _is_ used below, but pyright doesn't seem to notice..</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">inputs</span><span class="p">:</span> <span class="n">in_type</span>  <span class="c1"># pyright: ignore[reportInvalidTypeForm]</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">meta_type</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># pyright: ignore[reportInvalidTypeForm,reportUnknownVariableType]</span>
        <span class="n">expected_output</span><span class="p">:</span> <span class="n">out_type</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># pyright: ignore[reportInvalidTypeForm,reportUnknownVariableType]</span>
        <span class="k">if</span> <span class="n">evaluator_schema_types</span><span class="p">:</span>
            <span class="n">evaluators</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">tuple</span><span class="p">(</span><span class="n">evaluator_schema_types</span><span class="p">)]]</span> <span class="o">=</span> <span class="p">[]</span>  <span class="c1"># pyright: ignore  # noqa UP007</span>

    <span class="k">class</span><span class="w"> </span><span class="nc">Dataset</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">,</span> <span class="n">extra</span><span class="o">=</span><span class="s1">'forbid'</span><span class="p">):</span>
        <span class="n">cases</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Case</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">evaluator_schema_types</span><span class="p">:</span>
            <span class="n">evaluators</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">tuple</span><span class="p">(</span><span class="n">evaluator_schema_types</span><span class="p">)]]</span> <span class="o">=</span> <span class="p">[]</span>  <span class="c1"># pyright: ignore  # noqa UP007</span>

    <span class="n">json_schema</span> <span class="o">=</span> <span class="n">Dataset</span><span class="o">.</span><span class="n">model_json_schema</span><span class="p">()</span>
    <span class="c1"># See `_add_json_schema` below, since `$schema` is added to the JSON, it has to be supported in the JSON</span>
    <span class="n">json_schema</span><span class="p">[</span><span class="s1">'properties'</span><span class="p">][</span><span class="s1">'$schema'</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'type'</span><span class="p">:</span> <span class="s1">'string'</span><span class="p">}</span>
    <span class="k">return</span> <span class="n">json_schema</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




















  </div>

    </div>

</div>


























<div class="doc doc-object doc-function">


<h3 id="pydantic_evals.dataset.set_eval_attribute" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">set_eval_attribute</span>


</h3>
<div class="language-python doc-signature highlight"><pre id="__code_33"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_33 > code"></button><code><span class="nf">set_eval_attribute</span><span class="p">(</span><span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Set an attribute on the current task run.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name of the attribute.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>value</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The value of the attribute.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">973</span>
<span class="normal">974</span>
<span class="normal">975</span>
<span class="normal">976</span>
<span class="normal">977</span>
<span class="normal">978</span>
<span class="normal">979</span>
<span class="normal">980</span>
<span class="normal">981</span>
<span class="normal">982</span></pre></div></td><td class="code"><div><pre id="__code_34"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_34 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">set_eval_attribute</span><span class="p">(</span><span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set an attribute on the current task run.</span>

<span class="sd">    Args:</span>
<span class="sd">        name: The name of the attribute.</span>
<span class="sd">        value: The value of the attribute.</span>
<span class="sd">    """</span>
    <span class="n">current_case</span> <span class="o">=</span> <span class="n">_CURRENT_TASK_RUN</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">current_case</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">current_case</span><span class="o">.</span><span class="n">record_attribute</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h3 id="pydantic_evals.dataset.increment_eval_metric" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">increment_eval_metric</span>


</h3>
<div class="language-python doc-signature highlight"><pre id="__code_35"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_35 > code"></button><code><span class="nf">increment_eval_metric</span><span class="p">(</span>
    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n">amount</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Increment a metric on the current task run.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name of the metric.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>amount</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The amount to increment by.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/dataset.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">985</span>
<span class="normal">986</span>
<span class="normal">987</span>
<span class="normal">988</span>
<span class="normal">989</span>
<span class="normal">990</span>
<span class="normal">991</span>
<span class="normal">992</span>
<span class="normal">993</span>
<span class="normal">994</span></pre></div></td><td class="code"><div><pre id="__code_36"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_36 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">increment_eval_metric</span><span class="p">(</span><span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">amount</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Increment a metric on the current task run.</span>

<span class="sd">    Args:</span>
<span class="sd">        name: The name of the metric.</span>
<span class="sd">        amount: The amount to increment by.</span>
<span class="sd">    """</span>
    <span class="n">current_case</span> <span class="o">=</span> <span class="n">_CURRENT_TASK_RUN</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">current_case</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">current_case</span><span class="o">.</span><span class="n">increment_metric</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">amount</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>
















  </div>

    </div>

</div>







  
  






                
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
    
    
    <script id="__config" type="application/json">{"base": "../../..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../../../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../../../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>